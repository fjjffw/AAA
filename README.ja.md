# 🌐 自動翻訳

**無料の GitHub ドキュメント自動翻訳ツール** - プッシュするたびに、README/ドキュメントを複数の言語に自動的に翻訳します。

> 🆓 完全に無料、API キーは不要、Google 翻訳の無料パッケージに基づいて実装されています。

---

## 🚀 クイックスタート

### 1. リポジトリにコピーします

次のファイルをプロジェクトのルート ディレクトリにコピーします。

```
your-repo/
├── .github/workflows/translate.yml   ← GitHub Action 工作流
├── .translate.yml                     ← 翻译配置文件
└── scripts/translate.py               ← 翻译脚本
```

### 2. 構成を変更する

`.translate.yml` を編集して、翻訳するファイルとターゲット言語を指定します。

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

### 3. GitHub にプッシュする

```bash
git add .
git commit -m "add auto translate"
git push
```

`README.md` を変更してプッシュするたびに、GitHub Actions によって多言語バージョンが自動的に生成されます。

---

## 📖使用方法

### 自動翻訳 (GitHub Actions)

構成が完了すると、`main`/`master` ブランチにプッシュして `README.md` を変更するたびに、アクションが自動的に実行され、翻訳結果がウェアハウスに直接送信されます。

```
README.md          → README.zh-CN.md   (中文)
                   → README.ja.md      (日文)
                   → README.ko.md      (韩文)
                   → README.fr.md      (法文)
                   ...
```

### ローカル手動翻訳

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

### 手動トリガー

GitHub リポジトリ ページで → [アクション] → [ドキュメントの自動翻訳] → ワークフローを実行 → 言語を指定 → 実行します。

---

## ⚙️ 仕組み

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

## 🔧技術セレクション

|コンポーネント |選択 |理由 |
|------|------|------|
|翻訳エンジン | `deep-translator` (Google 翻訳) |無料、API キー不要、高品質、多言語 |
|設定ファイル |ヤムル |シンプルで読みやすい |
| CI/CD | GitHub アクション |十分な無料割り当て (2000 分/月) |
|コード保護 |通常のプレースホルダー |コードブロック/URL/画像が翻訳されていないことを確認してください。

---

## 📝 言語コードリファレンス

|言語 |コード |言語 |コード |
|------|------|------|------|
|中国語 (簡体字) | `zh-CN` |中国語 (繁体字) | `zh-TW` |
|日本語 | `ja` |韓国語 | `ko` |
|フランス語 | `fr` |ドイツ語 | `de` |
|スペイン語 | `es` |ポルトガル語 | `pt` |
|ロシア語 | `ru` |アラビア語 | `ar` |
|イタリア語 | `it` |オランダ語 | `nl` |
|タイ語 | `th` |ベトナム語 | `vi` |

---

## 📄 ライセンス

MIT — ご自由に使用、変更、配布してください。