# Day 3: FastAPI + 실무 Python

> **GitHub Repository**: [RAG-on-Local-CPU-minimal](https://github.com/rechard0609/RAG-on-Local-CPU-minimal)

> 스크립트 → API 서비스 전환

---

## 🎯 학습 목표

Day 3의 핵심은 다음과 같습니다:

> **"RAG 파이프라인을 API 형태로 실행·검증한다"**

이 Day를 마치면:
- ✅ FastAPI로 API 서버 구축
- ✅ dataclass / Pydantic 모델 이해
- ✅ `/query` 엔드포인트 구현
- ✅ Swagger UI 활용

---

## 📂 프로젝트 구조

```
Rag_minimal_day3/
├─ data/
│  └─ docs.txt       # RAG 입력 문서
├─ config.py         # 설정 값 분리
├─ models.py         # dataclass + Pydantic 모델
├─ loader.py         # 문서 로딩
├─ pipeline.py       # RAG 파이프라인
└─ main.py           # FastAPI 진입점
```

---

## 🔄 실행 흐름도

```
┌──────────────┐
│ HTTP Request │  POST /query
│   (JSON)      │  {"query": "..."}
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   main.py    │  FastAPI 엔드포인트
│ (API 서버)    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ pipeline.py  │  RAG 파이프라인
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  loader.py   │  문서 로딩
└──────┬───────┘
       │
       ▼
    JSON 응답
```

---

## ⚙️ 설치 및 실행

### 1. 패키지 설치

**Windows (PowerShell):**
```powershell
cd Rag_minimal_day3
pip install fastapi uvicorn
```

**macOS/Linux (Bash):**
```bash
cd Rag_minimal_day3
pip install fastapi uvicorn
# 또는
pip3 install fastapi uvicorn
```

### 2. 서버 실행

**Windows/macOS 공통:**
```bash
uvicorn main:app --reload
```

**예상 출력:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

---

## 🔍 API 테스트

### 1. Health Check

브라우저에서 접속:
```
http://127.0.0.1:8000/health
```

**응답:**
```json
{"status": "ok"}
```

### 2. Swagger UI

브라우저에서 접속:
```
http://127.0.0.1:8000/docs
```

**기능:**
- API 문서 자동 생성
- 브라우저에서 직접 테스트
- 요청/응답 예시 확인

### 3. Query API 테스트

**Swagger UI에서:**
1. `/query` 엔드포인트 클릭
2. "Try it out" 클릭
3. Request body 입력:
```json
{
  "query": "RAG란 무엇인가?"
}
```
4. "Execute" 클릭

**응답 예시:**
```json
{
  "answer": "입력 질문: RAG란 무엇인가?, 문서 수: 1"
}
```

---

## 🐛 디버깅 방법

### 방법 1: print() 디버깅

**main.py에 추가:**
```python
@app.post("/query", response_model=QueryResponse)
def query_api(req: QueryRequest):
    print(f"📥 받은 요청: {req.query}")  # 디버깅
    answer = pipeline(req.query)
    print(f"📤 응답: {answer}")  # 디버깅
    return QueryResponse(answer=answer)
```

**서버 터미널에서 확인:**
```
📥 받은 요청: RAG란 무엇인가?
📤 응답: 입력 질문: RAG란 무엇인가?, 문서 수: 1
INFO:     127.0.0.1:52341 - "POST /query HTTP/1.1" 200 OK
```

### 방법 2: VS Code 디버거

1. `main.py` 파일 열기
2. 브레이크포인트 설정
3. **F5** → "Python Debugger" 선택
4. 브라우저에서 API 호출
5. VS Code에서 변수 확인

---

## 🧠 핵심 개념

### FastAPI를 쓰는 이유

- ✅ Python AI/ML API 표준
- ✅ 자동 Swagger UI (`/docs`)
- ✅ 타입 체크 자동
- ✅ 비동기 지원

### dataclass vs Pydantic

**dataclass (내부 로직):**
```python
from dataclasses import dataclass

@dataclass
class Document:
    id: int
    text: str
```

**Pydantic (API 경계):**
```python
from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str
```

**차이점:**
- dataclass: Python 기본, 간단, 내부 사용
- Pydantic: API 검증, JSON 변환, FastAPI 필수

---

## ✅ Day 3 완료 기준

다음을 이해하고 실습했다면 완료입니다:

### 이해
- ✔️ FastAPI의 역할 (API 서버)
- ✔️ dataclass vs Pydantic 차이
- ✔️ `/query` 엔드포인트의 흐름
- ✔️ Swagger UI 활용법

### 실습
- ✔️ `uvicorn main:app --reload` 실행 성공
- ✔️ `/health` 접속 확인
- ✔️ Swagger UI에서 API 테스트
- ✔️ `/query` POST 요청/응답 확인

---

## 🔜 다음 단계 (Day 4)

Day 4는 **전자책 전용**입니다.

Day 5에서는:
- ✅ Embedding 생성
- ✅ Vector DB (FAISS) 연결
- ✅ 실제 문서 검색
- ✅ Top-K 검색

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