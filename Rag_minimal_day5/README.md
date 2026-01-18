# Day 5: Embedding & Vector DB

> **GitHub Repository**: [RAG-on-Local-CPU-minimal](https://github.com/rechard0609/RAG-on-Local-CPU-minimal)

> 실제 문서 검색 - RAG의 핵심

---

## 🎯 학습 목표

Day 5의 핵심은 다음과 같습니다:

> **"임베딩으로 문서를 검색하고, 검색 결과를 LLM에 전달한다"**

이 Day를 마치면:
- ✅ SentenceTransformer로 임베딩 생성
- ✅ FAISS로 벡터 검색
- ✅ Ingest (문서 색인) 과정
- ✅ Top-K 검색 이해

**핵심:** RAG = Retrieval (검색) + Generation (생성)

---

## 📂 프로젝트 구조

```
Rag_minimal_day5/
├─ main.py            # FastAPI 진입점
├─ pipeline.py        # RAG 파이프라인
├─ embedding.py       # 임베딩 생성
├─ vectorstore.py     # FAISS 벡터 검색
├─ ingest.py          # 문서 색인 (1회)
├─ loader.py          # 문서 로딩
├─ llm.py             # LLM Stub (더미)
├─ config.py          # 설정
└─ data/
   └─ docs.txt        # 입력 문서
```

---

## 🔄 실행 흐름도

```
┌──────────────┐
│ POST /query  │  {"query": "RAG란?"}
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ pipeline.py  │  RAG 파이프라인
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ embedding.py │  query → 벡터 변환
└──────┬───────┘
       │
       ▼
┌──────────────┐
│vectorstore.py│  Top-K 검색 (FAISS)
└──────┬───────┘
       │
       ▼
   검색된 문서
       │
       ▼
┌──────────────┐
│   llm.py     │  컨텍스트 기반 응답
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
cd Rag_minimal_day5
pip install fastapi uvicorn sentence-transformers faiss-cpu
```

**macOS/Linux (Bash):**
```bash
cd Rag_minimal_day5
pip install fastapi uvicorn sentence-transformers faiss-cpu
```

### 2. 서버 실행

```bash
uvicorn main:app --reload
```

### 3. API 테스트

**Swagger UI:**
```
http://127.0.0.1:8000/docs
```

**curl (PowerShell):**
```powershell
curl -X POST "http://127.0.0.1:8000/query" `
  -H "Content-Type: application/json" `
  -d '{"query":"RAG란 무엇인가?"}'
```

**curl (Bash):**
```bash
curl -X POST "http://127.0.0.1:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"query":"RAG란 무엇인가?"}'
```

---

## 🧠 핵심 개념

### 1. Embedding (임베딩)

**텍스트 → 숫자 벡터 변환:**
```python
text = "RAG는 검색 기반 생성이다"
vector = [0.23, -0.45, 0.78, ...]  # 384차원
```

**왜 필요한가?**
- 텍스트 유사도 계산 가능
- 의미 기반 검색
- 키워드 검색보다 정확

### 2. Vector Store (FAISS)

**벡터 저장 및 검색:**
```python
# 저장
index.add(embeddings)  # 문서 벡터들

# 검색
query_vector = embed(query)
distances, indices = index.search(query_vector, k=3)
```

**Top-K 검색:**
- K=3: 가장 유사한 3개 문서
- 거리 (distance): 유사도 지표
- L2 거리: 작을수록 유사

### 3. Ingest (색인)

**1회 실행:**
```
문서 로딩 → 임베딩 → 벡터 저장
```

**서버 시작 시 자동 실행**

### 4. RAG 파이프라인

```
Query → Embedding → Search → Context → LLM
```

**검색과 생성 분리:**
- 검색: Vector Store
- 생성: LLM
- 독립적 최적화 가능

---

## ✅ Day 5 완료 기준

다음을 이해하고 실습했다면 완료입니다:

### 이해
- ✔️ 임베딩이 무엇인지
- ✔️ Top-K 검색 방식
- ✔️ Ingest 과정의 역할
- ✔️ 검색과 생성의 분리

### 실습
- ✔️ `pip install` 성공
- ✔️ 서버 실행 성공
- ✔️ Swagger UI 접속
- ✔️ `/query` API 호출
- ✔️ 검색 결과 확인

---

## 🔜 다음 단계 (Day 6)

Day 6에서는:
- ✅ Reranker (재정렬)
- ✅ Hybrid Search (벡터 + 키워드)
- ✅ BM25 알고리즘
- ✅ Score Fusion

검색 품질 향상!

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