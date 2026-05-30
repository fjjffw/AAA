# 🌐 Traduction automatique

**Outil gratuit de traduction automatique de documents GitHub** - Traduisez automatiquement votre README/document en plusieurs langues à chaque poussée.

> 🆓 Entièrement gratuit, aucune clé API requise, implémenté sur la base du package gratuit Google Translate.

---

## 🚀 Démarrage rapide

### 1. Copiez dans votre référentiel

Copiez les fichiers suivants dans le répertoire racine de votre projet :

```
your-repo/
├── .github/workflows/translate.yml   ← GitHub Action 工作流
├── .translate.yml                     ← 翻译配置文件
└── scripts/translate.py               ← 翻译脚本
```

### 2. Modifier la configuration

Modifiez `.translate.yml` pour spécifier le fichier à traduire et la langue cible :

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

### 3. Poussez vers GitHub

```bash
git add .
git commit -m "add auto translate"
git push
```

Chaque fois que vous modifiez `README.md` et que vous poussez, GitHub Actions générera automatiquement une version multilingue.

---

## 📖 Comment utiliser

### Traduction automatique (Actions GitHub)

Une fois configurée, chaque fois que vous poussez vers la branche `main`/`master` et modifiez `README.md`, l'action s'exécutera automatiquement et les résultats de la traduction seront soumis directement à l'entrepôt :

```
README.md          → README.zh-CN.md   (中文)
                   → README.ja.md      (日文)
                   → README.ko.md      (韩文)
                   → README.fr.md      (法文)
                   ...
```

### Traduction manuelle locale

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

### Déclenchement manuel

Sur la page du référentiel GitHub → Actions → « Traduction automatique des documents » → Exécuter le workflow → Spécifier la langue → Exécuter.

---

## ⚙️ Comment ça marche

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

## 🔧Sélection Technique

| Composants | Sélection | Raisons |
|------|------|------|
| Moteur de traduction | `deep-translator` (Google Traduction) | Gratuit, aucune clé API requise, bonne qualité, plusieurs langues |
| Fichier de configuration | YAML | Simple et lisible |
| CI/CD | Actions GitHub | Quota gratuit suffisant (2000 min/mois) |
| Protection des codes | Espaces réservés réguliers | Assurez-vous que les blocs de code/URL/images ne sont pas traduits |

---

## 📝 Référence du code de langue

| langue | codes | langue | codes |
|------|------|------|------|
| Chinois (simplifié) | `zh-CN` | Chinois (traditionnel) | `zh-TW` |
| Japonais | `ja` | coréen | `ko` |
| français | `fr` | Allemand | `de` |
| Espagnol | `es` | Portugais | `pt` |
| Russe | `ru` | Arabe | `ar` |
| Italien | `it` | Néerlandais | `nl` |
| Thaï | `th` | Vietnamien | `vi` |

---

## 📄 Licence

MIT — N'hésitez pas à utiliser, modifier, distribuer.