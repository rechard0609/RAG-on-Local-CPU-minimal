# Day 8: LLM Gateway + 외부 API 연결

> **GitHub Repository**: [RAG-on-Local-CPU-minimal](https://github.com/rechard0609/RAG-on-Local-CPU-minimal)

> 실제 LLM 연결 - Gateway 패턴

---

## 🎯 학습 목표

Day 8의 핵심은 다음과 같습니다:

> **"외부 LLM API와 로컬 LLM을 Gateway로 통합하고, 실제로 연결한다"**

이 Day를 마치면:
- ✅ LLM Gateway 패턴 이해
- ✅ 외부 LLM API 연결 (OpenAI, Claude, Gemini 등)
- ✅ 로컬 LLM 통합
- ✅ API Key 관리
- ✅ 모델 교체 용이한 구조

**핵심:** LLM을 교체 가능한 자원으로 다루기

---

## 📂 프로젝트 구조

```
Rag_minimal_day8/
├─ docker-compose.yml     # Docker 실행
├─ config.yaml.example    # 설정 예시
├─ .gitignore             # Git 제외 파일
│
├─ gateway/               # LLM Gateway
│  ├─ main.py            # FastAPI 서버
│  ├─ router.py          # 라우팅
│  ├─ settings.py        # 설정 관리
│  ├─ usage.py           # 사용량 추적
│  ├─ metrics.py         # 메트릭
│  ├─ cost.py            # 비용 계산
│  ├─ logger.py          # 로깅
│  └─ llm/               # LLM 구현체
│     ├─ base.py         # 추상 클래스
│     ├─ openai_llm.py   # OpenAI
│     ├─ claude_llm.py   # Claude
│     ├─ gemini_llm.py   # Gemini
│     ├─ solar_llm.py    # SOLAR
│     └─ local_llm.py    # Local (llama.cpp)
│
├─ local_llm/            # 로컬 LLM 서버
│  ├─ Dockerfile
│  └─ run.sh
│
├─ ui/                   # 간단한 UI
│  ├─ index.html
│  ├─ app.js
│  └─ Dockerfile
│
├─ models/               # GGUF 모델 (Git 제외)
│  └─ tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf
│
└─ secrets/              # API Keys (Git 제외)
   └─ api_keys.yaml
```

---

## 🔄 실행 흐름도

```
┌─────────────┐
│   UI        │  모델 선택 + 질문
│ (3000)      │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Gateway    │  LLM Gateway
│  (8000)     │
└──────┬──────┘
       │
   ┌───┴────────────┬──────────┬─────────┐
   │                │          │         │
   ▼                ▼          ▼         ▼
┌────────┐    ┌─────────┐ ┌────────┐ ┌─────┐
│OpenAI  │    │ Claude  │ │ Gemini │ │Local│
│  API   │    │   API   │ │  API   │ │(CPU)│
└────────┘    └─────────┘ └────────┘ └─────┘
```

---

## ⚙️ 설치 및 실행

### 1. API Key 설정

**secrets/api_keys.yaml 생성:**
```yaml
openai:
  api_key: "sk-..."
  
claude:
  api_key: "sk-ant-..."
  
gemini:
  api_key: "AI..."
  
solar:
  api_key: "..."
```

**주의:**
- `secrets/` 폴더는 `.gitignore`에 포함됨
- API Key는 절대 Git에 올리지 마세요!

### 2. 모델 파일 준비 (로컬 LLM 사용 시)

```bash
# models/ 폴더에 GGUF 모델 배치
# 예: tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf
```

### 3. Docker Compose 실행

**Windows (PowerShell):**
```powershell
cd Rag_minimal_day8
docker compose up --build
```

**macOS/Linux:**
```bash
cd Rag_minimal_day8
docker compose up --build
```

### 4. 접속

**UI:**
```
http://localhost:3000
```

**Gateway API:**
```
http://localhost:8000/docs
```

**Status:**
```
http://localhost:8000/status
```

---

## 🧠 핵심 개념

### 1. LLM Gateway 패턴

**왜 Gateway가 필요한가?**
```python
# ❌ 나쁜 예
if model == "openai":
    response = openai.chat(...)
elif model == "claude":
    response = claude.messages(...)
elif model == "local":
    response = local.generate(...)

# ✅ 좋은 예
gateway = LLMGateway()
response = gateway.generate(prompt, model="openai")
```

**장점:**
- 모델 교체 용이
- 코드 중복 제거
- 사용량 추적 통합
- 확장 용이

### 2. 외부 LLM API 연결

**OpenAI:**
```python
import openai
response = openai.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)
```

**Claude:**
```python
import anthropic
response = anthropic.messages.create(
    model="claude-3-sonnet",
    messages=[{"role": "user", "content": prompt}]
)
```

**Gemini:**
```python
import google.generativeai as genai
response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
```

### 3. 로컬 LLM 통합

**llama.cpp 서버:**
```python
import requests
response = requests.post(
    "http://local_llm:11434/completion",
    json={"prompt": prompt}
)
```

### 4. API Key 관리

**절대 하지 말 것:**
```python
# ❌ 코드에 직접 박기
api_key = "sk-1234567890abcdef"
```

**올바른 방법:**
```python
# ✅ YAML 파일에서 로드
import yaml
with open("secrets/api_keys.yaml") as f:
    keys = yaml.safe_load(f)
    api_key = keys["openai"]["api_key"]
```

---

## ✅ Day 8 완료 기준

다음을 이해하고 실습했다면 완료입니다:

### 이해
- ✔️ Gateway 패턴의 장점
- ✔️ 외부 API vs 로컬 LLM 차이
- ✔️ API Key 관리 방법
- ✔️ 모델 교체 구조

### 실습
- ✔️ `secrets/api_keys.yaml` 생성
- ✔️ Docker Compose 실행
- ✔️ UI에서 모델 변경 테스트
- ✔️ 외부 API 호출 성공
- ✔️ 로컬 LLM 호출 성공

---

## 🔜 다음 단계 (Day 9)

Day 9에서는 (전자책 전용):
- ✅ Gateway + RAG 통합
- ✅ 문서 검색 + 외부 LLM 생성
- ✅ Vector DB 실전 활용
- ✅ 모델별 비교

완전한 RAG 시스템!

---

## ⚠️ 주의 사항

### Git 업로드 제외 항목

다음 파일/폴더는 `.gitignore`에 포함되어 Git에 올라가지 않습니다:

- ✅ `secrets/` - API Keys
- ✅ `api_keys.yaml` - API Keys
- ✅ `config.yaml` - 개인 설정
- ✅ `models/` - 대용량 모델 파일
- ✅ `__pycache__/` - Python 캐시

**원본은 유지**, Git 업로드만 제외됩니다!

### API 비용 주의

외부 LLM API는 사용량에 따라 비용이 발생합니다:

- GPT-4: $0.03 / 1K tokens (입력)
- Claude-3: $0.015 / 1K tokens (입력)
- Gemini: 무료 할당량 있음

테스트 시 비용에 유의하세요!

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