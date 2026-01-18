# Day 6: Reranker & Hybrid Search

> **GitHub Repository**: [RAG-on-Local-CPU-minimal](https://github.com/rechard0609/RAG-on-Local-CPU-minimal)

> 검색 품질 향상 - 2단계 검색

---

## 🎯 학습 목표

Day 6의 핵심은 다음과 같습니다:

> **"Vector Search + BM25 Reranker로 검색 품질을 향상시킨다"**

이 Day를 마치면:
- ✅ 2-Stage Retrieval 이해
- ✅ BM25 Reranker 적용
- ✅ Vector + Keyword 결합
- ✅ Top-K와 Top-N 차이

**핵심:** 넓게 검색 (Vector) → 정확하게 재정렬 (BM25)

---

## 📂 프로젝트 구조

```
Rag_minimal_day6/
├─ main.py            # FastAPI 진입점
├─ pipeline.py        # RAG 파이프라인
├─ embedding.py       # 임베딩 생성
├─ vectorstore.py     # Vector 검색
├─ reranker.py        # BM25 재정렬 ← 신규
├─ ingest.py          # 자산 생성
├─ loader.py          # 문서 로딩
├─ config.py          # 설정
└─ data/
   └─ docs.txt        # 입력 문서
```

---

## 🔄 실행 흐름도

```
┌──────────────┐
│ POST /chat   │  {"query": "RAG란?"}
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ pipeline.py  │  2-Stage Retrieval
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Stage 1      │  Vector Search
│vectorstore.py│  Top-K=10 (넓게 검색)
└──────┬───────┘
       │
       ▼
  Candidate 10개
       │
       ▼
┌──────────────┐
│ Stage 2      │  BM25 Reranker
│ reranker.py  │  Top-N=3 (정확하게)
└──────┬───────┘
       │
       ▼
  Final Context 3개
```

---

## ⚙️ 설치 및 실행

### 1. 패키지 설치

**Windows (PowerShell) / macOS/Linux:**
```bash
cd Rag_minimal_day6
pip install fastapi uvicorn sentence-transformers faiss-cpu rank-bm25
```

### 2. 서버 실행

```bash
uvicorn main:app --reload
```

### 3. API 테스트

**curl (PowerShell):**
```powershell
curl -X POST "http://127.0.0.1:8000/chat" `
  -H "Content-Type: application/json" `
  -d '{"query":"RAG에서 Embedding이 왜 필요해?"}'
```

**curl (Bash):**
```bash
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"query":"RAG에서 Embedding이 왜 필요해?"}'
```

---

## 🧠 핵심 개념

### 1. 2-Stage Retrieval

**왜 2단계로?**
```
Stage 1 (Vector Search):
  - 의미 기반 검색
  - 빠르지만 부정확
  - Top-K=10 (넓게)

Stage 2 (BM25 Rerank):
  - 키워드 기반 재정렬
  - 느리지만 정확
  - Top-N=3 (좁게)
```

**효과:**
- Vector: 관련 문서 놓치지 않음
- BM25: 질문과 정확히 매칭

### 2. BM25 Reranker

**역할:**
- 검색 ❌ (새로 찾지 않음)
- 재정렬 ✅ (순서만 바꿈)

**작동 방식:**
```python
# Vector Search 결과
candidates = ["Doc A", "Doc B", "Doc C"]

# BM25로 재정렬
query = "Embedding이 왜 필요해?"
scores = bm25.get_scores(query, candidates)
# → Doc B가 "Embedding" 단어 많음
# → Doc B가 1등으로 올라감
```

### 3. Top-K vs Top-N

```
Top-K (Vector): 후보 개수
  - K=10: 10개 후보 추출

Top-N (Rerank): 최종 개수
  - N=3: 3개만 선택
```

**설정 예시:**
- K=10, N=3: 10개 중 3개
- K=20, N=5: 20개 중 5개

---

## ✅ Day 6 완료 기준

다음을 이해하고 실습했다면 완료입니다:

### 이해
- ✔️ 2-Stage Retrieval 방식
- ✔️ BM25의 역할 (재정렬)
- ✔️ Vector + Keyword 결합
- ✔️ Top-K와 Top-N 차이

### 실습
- ✔️ `pip install rank-bm25` 성공
- ✔️ 서버 실행 성공
- ✔️ `/chat` API 호출
- ✔️ candidates vs contexts 확인
- ✔️ 재정렬 결과 비교

---

## 🔜 다음 단계 (Day 7)

Day 7에서는:
- ✅ 3-Stage Orchestration
- ✅ step_retrieve()
- ✅ step_rerank()
- ✅ step_generate()
- ✅ Trace 객체

파이프라인 고도화!

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