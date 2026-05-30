# 🌐 Traducción automática

**Herramienta gratuita de traducción automática de documentos de GitHub**: traduce automáticamente su archivo README/documento a varios idiomas en cada envío.

> 🆓 Completamente gratis, no se requiere clave API, implementado según el paquete gratuito de Google Translate.

---

## 🚀 Inicio rápido

### 1. Copia a tu repositorio

Copie los siguientes archivos al directorio raíz de su proyecto:

```
your-repo/
├── .github/workflows/translate.yml   ← GitHub Action 工作流
├── .translate.yml                     ← 翻译配置文件
└── scripts/translate.py               ← 翻译脚本
```

### 2. Modificar configuración

Edite `.translate.yml` para especificar el archivo a traducir y el idioma de destino:

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

### 3. Envíe a GitHub

```bash
git add .
git commit -m "add auto translate"
git push
```

Cada vez que modificas `README.md` y lo envías, GitHub Actions generará automáticamente una versión en varios idiomas.

---

## 📖 Cómo utilizar

### Traducción automática (Acciones de GitHub)

Una vez configurado, cada vez que acceda a la rama `main`/`master` y modifique `README.md`, la acción se ejecutará automáticamente y los resultados de la traducción se enviarán directamente al almacén:

```
README.md          → README.zh-CN.md   (中文)
                   → README.ja.md      (日文)
                   → README.ko.md      (韩文)
                   → README.fr.md      (法文)
                   ...
```

### Traducción manual local

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

### Gatillo manual

En la página del repositorio de GitHub → Acciones → "Traducir documentos automáticamente" → Ejecutar flujo de trabajo → Especificar el idioma → Ejecutar.

---

## ⚙️ Cómo funciona

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

## 🔧Selección Técnica

| Componentes | Selección | Razones |
|------|------|------|
| Motor de traducción | `deep-translator` (Traductor de Google) | Gratis, no se requiere clave API, buena calidad, varios idiomas |
| Archivo de configuración | YAML | Sencillo y legible |
| CI/CD | Acciones de GitHub | Cuota libre suficiente (2000 min/mes) |
| Protección de código | Marcadores de posición habituales | Asegúrese de que los bloques de código/URL/imágenes no estén traducidos |

---

## 📝 Referencia del código de idioma

| idioma | código | idioma | código |
|------|------|------|------|
| Chino (simplificado) | `zh-CN` | Chino (tradicional) | `zh-TW` |
| japonés | `ja` | coreano | `ko` |
| francés | `fr` | alemán | `de` |
| Español | `es` | portugués | `pt` |
| ruso | `ru` | árabe | `ar` |
| italiano | `it` | holandés | `nl` |
| tailandés | `th` | vietnamita | `vi` |

---

## 📄 Licencia

MIT: siéntase libre de utilizarlo, modificarlo y distribuirlo.