# Day 2: Python 문서 파이프라인 + Docker

> **GitHub Repository**: [RAG-on-Local-CPU-minimal](https://github.com/rechard0609/RAG-on-Local-CPU-minimal)

> 파일 읽기 + 설정 분리 + Docker 실행

---

## 🎯 학습 목표

Day 2의 핵심은 다음과 같습니다:

> **"문서를 파일에서 로딩하고, 설정으로 분리하고, Docker로 검증한다"**

이 Day를 마치면:
- ✅ 파일 I/O (with open 패턴) 이해
- ✅ `config.yaml`로 설정 분리
- ✅ `BASE_DIR` 경로 처리 방식 이해
- ✅ Docker 빌드 및 실행

**주의:** Day 2에는 LLM, Embedding, API가 없습니다!

---

## 📂 프로젝트 구조

```
Rag_minimal_day2/
├─ app/
│  ├─ main.py        # 실행 진입점
│  ├─ pipeline.py    # 처리 흐름
│  ├─ loader.py      # 문서 로딩
│  └─ config.py      # 설정 로더
│
├─ data/
│  └─ docs.txt       # 실습용 문서
│
├─ config.yaml       # 실행 설정
├─ requirements.txt
├─ Dockerfile
└─ README.md
```

**중요:** 모든 실행은 프로젝트 루트 기준!

---

## 🔄 실행 흐름도

```
┌──────────────┐
│   main.py    │  1. 실행 시작
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  config.py   │  2. config.yaml 로드
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ pipeline.py  │  3. 파이프라인 실행
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  loader.py   │  4. data/docs.txt 읽기
└──────┬───────┘
       │
       ▼
    문서 반환
       │
       ▼
    결과 출력
```

---

## 📄 설정 파일 (config.yaml)

```yaml
data:
  document_path: data/docs.txt

pipeline:
  max_docs: 2
```

- `document_path`: 로딩할 문서 파일 경로
- `max_docs`: 출력할 문서 최대 개수

**핵심:** 코드 수정 없이 설정만 바꿔 동작 제어!

---

## ⚙️ 로컬 실행

### Windows (PowerShell):
```powershell
cd Rag_minimal_day2
python app/main.py
```

### macOS/Linux (Bash):
```bash
cd Rag_minimal_day2
python app/main.py
# 또는
python3 app/main.py
```

### 예상 출력:
```
=== QUERY ===
RAG가 뭐야?

=== DOCUMENTS ===
- (1) RAG는 Retrieval Augmented Generation이다
- (2) 문서를 검색해서 답변한다
```

---

## 🐳 Docker 실행 (Day 2 핵심)

### 1. Docker 이미지 빌드

**Windows (PowerShell):**
```powershell
docker build -t rag-minimal-day2 .
```

**macOS/Linux (Bash):**
```bash
docker build -t rag-minimal-day2 .
```

### 2. 컨테이너 실행

```bash
docker run --rm rag-minimal-day2
```

- `--rm`: 실행 후 컨테이너 자동 삭제

### 예상 출력:
로컬 실행과 동일한 결과가 나와야 합니다!

---

## 🐛 디버깅 방법

### 방법 1: print() 디버깅

**loader.py에 추가:**
```python
def load_documents(path):
    BASE_DIR = Path(__file__).resolve().parent.parent
    doc_path = BASE_DIR / path
    
    print(f"📂 BASE_DIR: {BASE_DIR}")           # 디버깅
    print(f"📂 Full path: {doc_path}")          # 디버깅
    print(f"📂 File exists: {doc_path.exists()}")  # 디버깅
    
    with open(doc_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    print(f"✅ Loaded {len(content)} characters")  # 디버깅
    return content.split("\n")
```

### 방법 2: VS Code 디버거

**사전 준비:**
- VS Code Python 확장 설치
- Python Interpreter 선택

**디버깅 시작:**
1. `app/main.py` 파일 열기
2. 브레이크포인트 설정
3. **F5** → "Python Debugger" 선택
4. 변수 확인 (VARIABLES 패널)

---

## 🧠 핵심 개념

### BASE_DIR 패턴

```python
# loader.py
BASE_DIR = Path(__file__).resolve().parent.parent
doc_path = BASE_DIR / path
```

**왜 중요한가?**
- 실행 위치(CWD)에 의존하지 않음
- 로컬/Docker 어디서나 동일하게 작동
- 실무 필수 패턴

### 설정 분리 (config.yaml)

```python
# config.py
def load_config():
    with open("config.yaml") as f:
        return yaml.safe_load(f)
```

**장점:**
- 코드 수정 없이 동작 변경 가능
- 환경별 설정 관리 용이
- 프로덕션 베스트 프랙티스

---

## ✅ Day 2 완료 기준

다음을 이해하고 실습했다면 완료입니다:

### 이해
- ✔️ 파일 I/O (`with open`) 사용법
- ✔️ `config.yaml` 설정 분리 목적
- ✔️ `BASE_DIR` 경로 처리 방식
- ✔️ Docker 빌드와 실행의 차이

### 실습
- ✔️ 로컬에서 `python app/main.py` 성공
- ✔️ `config.yaml` 수정 후 결과 변화 확인
- ✔️ Docker 이미지 빌드 성공
- ✔️ Docker 컨테이너 실행 성공
- ✔️ 로컬과 Docker 실행 결과 동일

---

## 🔜 다음 단계 (Day 3)

Day 3에서는 다음을 추가합니다:

- ✅ FastAPI로 API 서버 구축
- ✅ `/query` 엔드포인트 생성
- ✅ dataclass / Pydantic 모델
- ✅ Swagger UI (`/docs`)

"스크립트 → 서비스" 전환!

---

## 📜 라이선스

Copyright © 2022 정상혁 (Sanghyuk Jung)

본 저작물은 [크리에이티브 커먼즈 저작자표시-비영리-변경금지 4.0 국제 라이선스](https://creativecommons.org/licenses/by-nc-nd/4.0/)에 따라 이용할 수 있습니다.

### 허용
- ✅ 개인 학습 목적 사용
- ✅ 출처 표시 후 비영리 공유

### 금지
- ❌ 상업적 이용
- ❌ 내용 수정 및 2차 저작
- ❌ 저작자 허락 없는 재배포

**상업적 이용 문의**: j4angguiop@gmail.com

---

**⭐ 이 프로젝트가 도움이 되었다면 Star를 눌러주세요!**

**Copyright © 2022-2026 정상혁 (Sanghyuk Jung). All Rights Reserved.**