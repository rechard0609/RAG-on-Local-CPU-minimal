# RAG-on-Local-CPU-minimal
> 신입사원을 위한 RAG 구조 학습 - 디버깅으로 배우는 최소 구현

---

## 🚨 핵심 고지사항

### 본 저장소는 "구조 학습용" 최소 코드만 제공합니다

**제공되는 것:**
- ✅ 프로젝트 폴더 구조
- ✅ Day 1, 2, 3, 5, 6, 7, 8 구조 코드
- ✅ 이론 문서 (docs/)

**제공되지 않는 것:**
- ❌ **Day 4, 9, 10 전체 코드** (전자책 전용)
- ❌ **실습 예제 솔루션**
- ❌ **연습 문제 정답**
- ❌ **케이스 스터디 전체 소스**
- ❌ **프로덕션 레벨 구현**

**전체 코드 제공:** 전자책 구매 시 (j4angguiop@gmail.com)

---

## ⚠️ 프로젝트 성격

**본 프로젝트는 RAG 시스템의 "구조 이해"와 "동작 흐름 파악"을 위한 교육용 최소 구현입니다.**

- ✅ 실제 외부 API 연결 (OpenAI 등) - API Key 필요
- ✅ 실제 Vector DB 설치 및 사용 (FAISS, Milvus 등)
- ✅ 각 컴포넌트의 역할과 연결 방식 학습
- ✅ 파이프라인 동작 원리 체득
- ❌ 프로덕션 레벨 코드 아님 (에러 처리, 최적화, 보안 최소화)
- ❌ 실무용 복잡한 로직 제외 (핵심 흐름만 구현)

**🎯 목적: "구조 파악" + "흐름 체득"**

---

## 🎯 프로젝트 목표

**"코드를 디버깅하면서 RAG 동작 원리를 체득한다"**

복잡한 이론 설명 없이, 실제 동작하는 최소 구현 코드를 한 줄씩 따라가며  
RAG 시스템의 구조와 흐름을 이해합니다.

### 이 프로젝트를 마치면

- ✅ **"아, RAG가 이렇게 동작하는구나!"** 체감
- ✅ Embedding → Vector Store → Retrieval → Generation 전체 흐름 이해
- ✅ 각 컴포넌트 역할과 연결 구조 파악
- ✅ 디버깅 포인트로 학습하는 방법 습득
- ✅ **"RAG 하나 직접 만들었다"** 라고 말할 수 있는 상태

---

## 📅 10일 커리큘럼

| Day | 주제 | 핵심 내용 | 코드 제공 |
|-----|------|-----------|-----------|
| **Day 1** | RAG 파이프라인 최소 구조 | • 파이프라인 개념<br>• main → pipeline → loader 흐름<br>• 3파일 구조로 RAG 뼈대 파악 | ✅ **제공** |
| **Day 2** | Python 문서 파이프라인 + Docker | • 파일 I/O<br>• config.yaml 분리<br>• Docker 빌드 & 실행 | ✅ **제공** |
| **Day 3** | FastAPI + 실무 Python | • FastAPI 서버 구축<br>• dataclass / Pydantic<br>• `/query` API | ✅ **제공** |
| **Day 4** | 로컬 LLM 서빙 (CPU) + Docker | • 경량 모델 (GGUF)<br>• llama.cpp<br>• Docker로 LLM 서빙 | ❌ **전자책 전용** |
| **Day 5** | Embedding & Vector DB | • SentenceTransformer<br>• FAISS 설치 및 사용<br>• Ingest (문서 색인) | ✅ **제공** |
| **Day 6** | Reranker & Hybrid Search | • Vector + Keyword Search<br>• BM25 Reranker<br>• Score Fusion | ✅ **제공** |
| **Day 7** | Orchestration (3-Stage) | • 3단계 파이프라인<br>• step_retrieve()<br>• step_generate() | ✅ **제공** |
| **Day 8** | LLM Gateway + 외부 API 연결 | • Gateway 구조 학습<br>• 외부 LLM API 연결 (OpenAI 등)<br>• API Key 기반 인증 | ✅ **제공** |
| **Day 9** | Gateway + RAG 통합 | • Gateway에 RAG 연결<br>• Vector DB 실제 사용<br>• 모델별 비교 | ❌ **전자책 전용** |
| **Day 10** | 최종 통합 시스템 | • 전체 시스템 통합<br>• 외부 API + 로컬 모델 혼용<br>• Vector DB 실전 활용 | ❌ **전자책 전용** |

**📌 Day 4, 9, 10은 전자책 구매 시 제공됩니다.**

---

## 💡 학습 포인트

### ✅ 실제로 구현하는 것
- 외부 LLM API 연결 (OpenAI, Anthropic 등)
- Vector DB 설치 및 사용 (FAISS, Milvus)
- 문서 검색 → LLM 생성 전체 흐름
- Gateway 패턴으로 모델 교체

### ❌ 생략하는 것 (학습 효율화)
- 프로덕션 레벨 에러 처리
- 성능 최적화 (캐싱, 배치 처리 등)
- 보안 강화 (인증/인가 고도화)
- 복잡한 예외 상황 처리

### 🎯 학습 목표
**"어떻게 동작하는가"를 체득 → 실무 확장 가능**

---

## 🚀 빠른 시작

### 필요 환경

- **CPU**: 4코어 이상
- **RAM**: 16GB 이상
- **Python**: 3.10+
- **VS Code** (권장)
- **API Key**: OpenAI 또는 Anthropic (Day 8 이후)

### 설치 및 실행
```bash
# 1. 저장소 클론
git clone https://github.com/rechard0609/RAG-on-Local-CPU-minimal.git
cd RAG-on-Local-CPU-minimal

# 2. Day 1부터 시작
cd Rag_minimal_day1

# 3. README.md 읽고 따라하기
```

---

## 🔍 학습 방식

### 디버깅 중심 학습
```
1. 코드 실행 → 브레이크포인트 설정
2. 한 줄씩 Step Into/Over
3. 변수 값 확인 → "아, 이게 이렇게 바뀌는구나"
4. 다음 함수로 → 전체 흐름 파악
```

### 최소 구현의 장점

- 불필요한 코드 제거 → 핵심만 남김
- 간단한 구조 → 빠른 이해
- 실제 동작 → 즉시 확인 가능

---

## 📂 프로젝트 구조
```
RAG-on-Local-CPU-minimal/
├─ docs/                      # 📖 학습 자료
│  └─ setup-guide.md          # 환경 설정 가이드
│
├─ Rag_minimal_day1/          # ✅ 제공
├─ Rag_minimal_day2/          # ✅ 제공
├─ Rag_minimal_day3/          # ✅ 제공
├─ Rag_minimal_day4/          # ❌ 전자책 전용
├─ Rag_minimal_day5/          # ✅ 제공
├─ Rag_minimal_day6/          # ✅ 제공
├─ Rag_minimal_day7/          # ✅ 제공
├─ Rag_minimal_day8/          # ✅ 제공
├─ Rag_minimal_day9/          # ❌ 전자책 전용
└─ Rag_minimal_day10/         # ❌ 전자책 전용
```

---

## 🎓 학습 대상

### 이런 분들께 추천

- ✅ 신입 개발자 (RAG 처음 접하는 분)
- ✅ 이론은 알지만 실제 구현은 모르는 분
- ✅ 코드 읽으며 구조 파악하고 싶은 분
- ✅ 디버깅으로 학습하는 걸 선호하는 분

### 사전 지식

- Python 기본 문법 (변수, 함수, 클래스)
- REST API 개념 (선택)
- LLM 기본 개념 (선택)

---

## ✅ 최종 완료 상태

이 커리큘럼을 마치면:

- ✅ **"RAG 하나 직접 만들었다"**
- ✅ Python 실무 코드 거부감 제거
- ✅ LLM/RAG 구조 완벽 이해
- ✅ SI·PoC·제안서 투입 가능

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

## 🔗 관련 링크

- **GitHub**: https://github.com/rechard0609
- **이메일**: j4angguiop@gmail.com
- **블로그**: https://j4zlap.tistory.com

---

## 🔒 전자책 구매 안내

### 전자책에서만 제공되는 내용

- ✅ **Day 4**: 로컬 LLM 서빙 전체 구현
- ✅ **Day 9**: Gateway + RAG 완전 통합
- ✅ **Day 10**: Agent + Orchestration 고급 구현
- ✅ **모든 실습 예제 솔루션**
- ✅ **연습 문제 정답 및 해설**
- ✅ **케이스 스터디 전체 소스**

### 구매 문의

📧 **Email**: j4angguiop@gmail.com  
📝 **Blog**: https://j4zlap.tistory.com

---

**⭐ 이 프로젝트가 도움이 되었다면 Star를 눌러주세요!**

**Copyright © 2022-2026 정상혁 (Sanghyuk Jung). All Rights Reserved.**