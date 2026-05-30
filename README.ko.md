# 🌐 자동 번역

**무료 GitHub 문서 자동 번역 도구** - 푸시할 때마다 README/문서를 여러 언어로 자동 번역합니다.

> 🆓 완전 무료이며 API 키가 필요하지 않으며 Google 번역 무료 패키지를 기반으로 구현되었습니다.

---

## 🚀 빠른 시작

### 1. 저장소에 복사합니다.

다음 파일을 프로젝트의 루트 디렉터리에 복사합니다.

```
your-repo/
├── .github/workflows/translate.yml   ← GitHub Action 工作流
├── .translate.yml                     ← 翻译配置文件
└── scripts/translate.py               ← 翻译脚本
```

### 2. 구성 수정

`.translate.yml`을 편집하여 번역할 파일과 대상 언어를 지정합니다.

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

### 3. GitHub로 푸시

```bash
git add .
git commit -m "add auto translate"
git push
```

`README.md`을 수정하고 푸시할 때마다 GitHub Actions는 자동으로 다국어 버전을 생성합니다.

---

## 📖 사용방법

### 자동 번역(GitHub Actions)

일단 구성되면 `main`/`master` 분기로 푸시하고 `README.md`을 수정할 때마다 작업이 자동으로 실행되고 번역 결과가 창고로 직접 다시 제출됩니다.

```
README.md          → README.zh-CN.md   (中文)
                   → README.ja.md      (日文)
                   → README.ko.md      (韩文)
                   → README.fr.md      (法文)
                   ...
```

### 현지 매뉴얼 번역

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

### 수동 트리거

GitHub 저장소 페이지 → 작업 → "문서 자동 번역" → 워크플로 실행 → 언어 지정 → 실행.

---

## ⚙️ 작동 원리

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

## 🔧기술 선정

| 구성요소 | 선택 | 이유 |
|------|------|------|
| 번역 엔진 | `deep-translator` (구글 번역) | 무료, API 키 필요 없음, 우수한 품질, 다국어 |
| 구성 파일 | YAML | 간단하고 읽기 쉽습니다 |
| CI/CD | GitHub 작업 | 충분한 무료 할당량(2000분/월) |
| 코드 보호 | 일반 자리 표시자 | 코드 블록/URL/이미지가 번역되지 않았는지 확인 |

---

## 📝 언어 코드 참조

| 언어 | 코드 | 언어 | 코드 |
|------|------|------|------|
| 중국어(간체) | `zh-CN` | 중국어(번체) | `zh-TW` |
| 일본어 | `ja` | 한국어 | `ko` |
| 프랑스어 | `fr` | 독일어 | `de` |
| 스페인어 | `es` | 포르투갈어 | `pt` |
| 러시아어 | `ru` | 아랍어 | `ar` |
| 이탈리아어 | `it` | 네덜란드어 | `nl` |
| 태국어 | `th` | 베트남어 | `vi` |

---

## 📄 라이센스

MIT — 자유롭게 사용, 수정, 배포할 수 있습니다.