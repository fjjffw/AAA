# 🌐 Automatische Übersetzung

**Kostenloses GitHub-Tool zur automatischen Übersetzung von Dokumenten** – Übersetzen Sie Ihre README-Datei/Ihr Dokument bei jedem Push automatisch in mehrere Sprachen.

> 🆓 Völlig kostenlos, kein API-Schlüssel erforderlich, implementiert auf Basis des kostenlosen Google Translate-Pakets.

---

## 🚀 Schnellstart

### 1. In Ihr Repository kopieren

Kopieren Sie die folgenden Dateien in das Stammverzeichnis Ihres Projekts:

```
your-repo/
├── .github/workflows/translate.yml   ← GitHub Action 工作流
├── .translate.yml                     ← 翻译配置文件
└── scripts/translate.py               ← 翻译脚本
```

### 2. Konfiguration ändern

Bearbeiten Sie `.translate.yml`, um die zu übersetzende Datei und die Zielsprache anzugeben:

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

### 3. Auf GitHub übertragen

```bash
git add .
git commit -m "add auto translate"
git push
```

Jedes Mal, wenn Sie `README.md` ändern und pushen, generiert GitHub Actions automatisch eine mehrsprachige Version.

---

## 📖 Anwendung

### Automatische Übersetzung (GitHub-Aktionen)

Nach der Konfiguration wird jedes Mal, wenn Sie zum Zweig `main`/`master` pushen und `README.md` ändern, die Aktion automatisch ausgeführt und die Übersetzungsergebnisse werden direkt an das Warehouse zurückgesendet:

```
README.md          → README.zh-CN.md   (中文)
                   → README.ja.md      (日文)
                   → README.ko.md      (韩文)
                   → README.fr.md      (法文)
                   ...
```

### Lokale manuelle Übersetzung

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

### Manueller Auslöser

Auf der GitHub-Repository-Seite → Aktionen → „Dokumente automatisch übersetzen“ → Workflow ausführen → Sprache angeben → Ausführen.

---

## ⚙️ So funktioniert es

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

## 🔧Technische Auswahl

| Komponenten | Auswahl | Gründe |
|------|------|------|
| Übersetzungsmaschine | `deep-translator` (Google Translate) | Kostenlos, kein API-Schlüssel erforderlich, gute Qualität, mehrere Sprachen |
| Konfigurationsdatei | YAML | Einfach und lesbar |
| CI/CD | GitHub-Aktionen | Ausreichendes kostenloses Kontingent (2000 Min./Monat) |
| Codeschutz | Reguläre Platzhalter | Stellen Sie sicher, dass Codeblöcke/URLs/Bilder nicht übersetzt werden |

---

## 📝 Sprachcode-Referenz

| Sprache | Code | Sprache | Code |
|------|------|------|------|
| Chinesisch (vereinfacht) | `zh-CN` | Chinesisch (traditionell) | `zh-TW` |
| Japanisch | `ja` | Koreanisch | `ko` |
| Französisch | `fr` | Deutsch | `de` |
| Spanisch | `es` | Portugiesisch | `pt` |
| Russisch | `ru` | Arabisch | `ar` |
| Italienisch | `it` | Niederländisch | `nl` |
| Thailändisch | `th` | Vietnamesisch | `vi` |

---

## 📄 Lizenz

MIT – Fühlen Sie sich frei, es zu verwenden, zu ändern und zu verbreiten.