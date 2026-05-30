#!/usr/bin/env python3
"""
自动翻译脚本 —— 将 Markdown/文本文件翻译为多语言版本。
使用 deep-translator (Google Translate 免费封装)，无需 API Key。

用法:
    python scripts/translate.py                    # 翻译 .translate.yml 中配置的文件
    python scripts/translate.py --file README.md   # 翻译单个文件
    python scripts/translate.py --file README.md --langs zh-CN,ja,ko
"""

import os
import re
import sys
import yaml
import argparse
from pathlib import Path

# deep-translator 是对 Google Translate 的免费封装
try:
    from deep_translator import GoogleTranslator
except ImportError:
    print("请先安装: pip install deep-translator pyyaml")
    sys.exit(1)

# ---------- 配置 ----------
DEFAULT_CONFIG = ".translate.yml"
DEFAULT_LANGS = ["zh-CN", "ja", "ko", "fr", "es", "de", "pt", "ru", "ar"]
MAX_CHUNK = 4000  # Google Translate 单次最大字符数（保守值）


def load_config(config_path: str) -> dict:
    """加载翻译配置文件"""
    if not os.path.exists(config_path):
        return {"files": ["README.md"], "languages": DEFAULT_LANGS[:6]}
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def split_text(text: str, max_len: int = MAX_CHUNK) -> list:
    """
    将文本按段落边界切分，每段不超过 max_len。
    保留 Markdown 代码块不被切割。
    """
    chunks = []
    current = ""
    in_code_block = False

    for line in text.split("\n"):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block

        if len(current) + len(line) + 1 > max_len and current:
            chunks.append(current)
            current = line + "\n"
        else:
            current += line + "\n"

    if current.strip():
        chunks.append(current)

    return chunks


def protect_code_blocks(text: str) -> tuple:
    """
    将代码块和行内代码替换为占位符，避免被翻译。
    返回 (带占位符的文本, {占位符: 原始内容})
    """
    placeholders = {}
    counter = [0]

    # 保护围栏代码块
    def repl_fence(m):
        key = f"__CODE_FENCE_{counter[0]}__"
        placeholders[key] = m.group(0)
        counter[0] += 1
        return key

    text = re.sub(r"```[\s\S]*?```", repl_fence, text)

    # 保护行内代码
    def repl_inline(m):
        key = f"__CODE_INLINE_{counter[0]}__"
        placeholders[key] = m.group(0)
        counter[0] += 1
        return key

    text = re.sub(r"`[^`]+`", repl_inline, text)

    # 保护 URL
    def repl_url(m):
        key = f"__URL_{counter[0]}__"
        placeholders[key] = m.group(0)
        counter[0] += 1
        return key

    text = re.sub(r"https?://[^\s\)]+", repl_url, text)

    # 保护图片语法 ![alt](url)
    def repl_img(m):
        key = f"__IMG_{counter[0]}__"
        placeholders[key] = m.group(0)
        counter[0] += 1
        return key

    text = re.sub(r"!\[.*?\]\(.*?\)", repl_img, text)

    return text, placeholders


def restore_placeholders(text: str, placeholders: dict) -> str:
    """还原占位符为原始内容"""
    for key, value in placeholders.items():
        text = text.replace(key, value)
    return text


def translate_text(text: str, target_lang: str) -> str:
    """
    将文本翻译为目标语言。
    自动分块处理长文本，保护代码块不被翻译。
    """
    if not text.strip():
        return text

    # 保护特殊内容
    protected, placeholders = protect_code_blocks(text)
    chunks = split_text(protected)
    translated_chunks = []

    translator = GoogleTranslator(source="auto", target=target_lang)

    for i, chunk in enumerate(chunks):
        if not chunk.strip():
            translated_chunks.append(chunk)
            continue
        try:
            result = translator.translate(chunk)
            translated_chunks.append(result)
        except Exception as e:
            print(f"  WARN chunk {i+1}/{len(chunks)} failed: {e}")
            translated_chunks.append(chunk)  # 保留原文

    result = "\n".join(translated_chunks)
    result = restore_placeholders(result, placeholders)
    return result


def get_output_path(input_path: str, lang: str) -> str:
    """
    生成翻译后文件的输出路径。
    README.md -> README.zh-CN.md
    docs/guide.md -> docs/guide.zh-CN.md
    """
    p = Path(input_path)
    stem = p.stem
    return str(p.parent / f"{stem}.{lang}{p.suffix}")


def translate_file(filepath: str, languages: list, dry_run: bool = False):
    """翻译单个文件到所有目标语言"""
    if not os.path.exists(filepath):
        print(f"  FAIL: file not found: {filepath}")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"\n[File] {filepath} ({len(content)} chars)")

    for lang in languages:
        out_path = get_output_path(filepath, lang)

        if dry_run:
            print(f"  -> [{lang}] {out_path}  (dry-run)")
            continue

        print(f"  -> [{lang}] translating...", end=" ", flush=True)
        translated = translate_text(content, lang)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(translated)

        print(f"OK ({len(translated)} chars) -> {out_path}")


def main():
    parser = argparse.ArgumentParser(description="自动翻译 Markdown 文档")
    parser.add_argument("--file", "-f", help="指定翻译单个文件")
    parser.add_argument("--langs", help="目标语言列表，逗号分隔 (例: zh-CN,ja,ko)")
    parser.add_argument("--config", default=DEFAULT_CONFIG, help="配置文件路径")
    parser.add_argument("--dry-run", action="store_true", help="预览模式，不实际翻译")
    args = parser.parse_args()

    # 加载配置
    cfg = load_config(args.config)

    # 确定要翻译的文件
    if args.file:
        files = [args.file]
    else:
        files = cfg.get("files", ["README.md"])

    # 确定目标语言
    if args.langs:
        languages = [l.strip() for l in args.langs.split(",")]
    else:
        languages = cfg.get("languages", DEFAULT_LANGS[:6])

    print("=" * 60)
    print("[Auto Translate] docs translation tool")
    print(f"   Files: {', '.join(files)}")
    print(f"   Languages: {', '.join(languages)}")
    print("=" * 60)

    for f in files:
        translate_file(f, languages, dry_run=args.dry_run)

    print("\nDone! All translations completed.")


if __name__ == "__main__":
    main()
