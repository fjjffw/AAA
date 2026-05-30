# 🌐 Auto Translate

**免费的 GitHub 文档自动翻译工具** —— 每次 push 自动把你的 README / 文档翻译成多国语言。

> 🆓 完全免费，无需任何 API Key，基于 Google Translate 免费封装实现。

---

## 🚀 快速开始

### 1. 复制到你的仓库

把以下文件复制到你项目的根目录：

```
your-repo/
├── .github/workflows/translate.yml   ← GitHub Action 工作流
├── .translate.yml                     ← 翻译配置文件
└── scripts/translate.py               ← 翻译脚本
```

### 2. 修改配置

编辑 `.translate.yml`，指定要翻译的文件和目标语言：

```yaml
files:
  - README.md
  # - docs/guide.md

languages:
  - zh-CN   # 简体中文
  - ja      # 日文
  - ko      # 韩文
  - fr      # 法文
```

### 3. Push 到 GitHub

```bash
git add .
git commit -m "add auto translate"
git push
```

之后每次修改 `README.md` 并 push，GitHub Actions 会自动生成多语言版本。

---

## 📖 使用方式

### 自动翻译 (GitHub Actions)

一旦配置好，每次 push 到 `main`/`master` 分支且修改了 `README.md` 时，Action 自动运行，将翻译结果直接提交回仓库：

```
README.md          → README.zh-CN.md   (中文)
                   → README.ja.md      (日文)
                   → README.ko.md      (韩文)
                   → README.fr.md      (法文)
                   ...
```

### 本地手动翻译

```bash
# 安装依赖
pip install deep-translator pyyaml

# 翻译 .translate.yml 中配置的所有文件
python scripts/translate.py

# 翻译单个文件到指定语言
python scripts/translate.py --file README.md --langs zh-CN,ja,ko

# 预览模式（不实际翻译）
python scripts/translate.py --dry-run
```

### 手动触发

在 GitHub 仓库页面 → Actions → "Auto Translate Docs" → Run workflow → 可指定语言 → Run。

---

## ⚙️ 工作原理

```
push README.md
       │
       ▼
 GitHub Actions 触发
       │
       ▼
 scripts/translate.py
       │
       ├─ 读取 .translate.yml 配置
       ├─ 保护代码块 / URL / 图片 (不翻译)
       ├─ 调用 GoogleTranslator (deep-translator)
       │   ├─ 自动分块 (超长文本分批翻译)
       │   └─ 逐语言翻译
       └─ 保存 README.{lang}.md
       │
       ▼
 git commit & push 回仓库
```

---

## 🔧 技术选型

| 组件 | 选型 | 原因 |
|------|------|------|
| 翻译引擎 | `deep-translator` (Google Translate) | 免费、无需 API Key、质量好、语言多 |
| 配置文件 | YAML | 简单可读 |
| CI/CD | GitHub Actions | 免费额度充足 (2000 min/月) |
| 代码保护 | 正则占位符 | 保证代码块/URL/图片不被翻译 |

---

## 📝 语言代码参考

| 语言 | 代码 | 语言 | 代码 |
|------|------|------|------|
| 中文(简体) | `zh-CN` | 中文(繁体) | `zh-TW` |
| 日文 | `ja` | 韩文 | `ko` |
| 法文 | `fr` | 德文 | `de` |
| 西班牙文 | `es` | 葡萄牙文 | `pt` |
| 俄文 | `ru` | 阿拉伯文 | `ar` |
| 意大利文 | `it` | 荷兰文 | `nl` |
| 泰文 | `th` | 越南文 | `vi` |

---

## 📄 License

MIT — 随意使用、修改、分发。