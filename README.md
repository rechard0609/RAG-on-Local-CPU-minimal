# RAG-on-Local-CPU-minimal
> 신입사원을 위한 RAG 구조 학습 - 디버깅으로 배우는 최소 구현

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

---

## 🚨 핵심 고지사항

> ### **본 저장소는 "구조 학습용" 최소 코드만 제공합니다**
> 
> **제공되는 것:**
> - ✅ 프로젝트 폴더 구조
> - ✅ 이론 문서 (docs/)
> - ✅ Day 1, 2, 3, 5, 6, 7, 8 구조 코드
> 
> **제공되지 않는 것:**
> - ❌ **Day 4, 9, 10 전체 코드** (전자책 전용)
> - ❌ **실습 예제 솔루션**
> - ❌ **연습 문제 정답**
> - ❌ **케이스 스터디 전체 소스**
> - ❌ **프로덕션 레벨 구현**
> 
> **전체 코드 제공:** 전자책 구매 시 (j4angguiop@gmail.com)

---

## ⚠️ 프로젝트 성격

> **본 프로젝트는 RAG 시스템의 "구조 이해"와 "동작 흐름 파악"을 위한 교육용 최소 구현입니다.**
> 
> - ✅ 실제 외부 API 연결 (OpenAI 등) - API Key 필요
> - ✅ 실제 Vector DB 설치 및 사용 (FAISS, Milvus 등)
> - ✅ 각 컴포넌트의 역할과 연결 방식 학습
> - ✅ 파이프라인 동작 원리 체득
> - ❌ 프로덕션 레벨 코드 아님 (에러 처리, 최적화, 보안 최소화)
> - ❌ 실무용 복잡한 로직 제외 (핵심 흐름만 구현)
> - 🎯 **목적: "구조 파악" + "흐름 체득"**

---

## 🎯 프로젝트 목표

**"코드를 디버깅하면서 RAG 동작 원리를 체득한다"**

복잡한 이론 설명 없이, 실제 동작하는 최소 구현 코드를 한 줄씩 따라가며 RAG 시스템의 구조와 흐름을 이해합니다.

### 이 프로젝트를 마치면

- ✅ **"아, RAG가 이렇게 동작하는구나!"** 체감
- ✅ Embedding → Vector Store → Retrieval → Generation 전체 흐름 이해
- ✅ 각 컴포넌트 역할과 연결 구조 파악
- ✅ 디버깅 포인트로 학습하는 방법 습득
- ✅ **"RAG 하나 직접 만들었다"** 라고 말할 수 있는 상태

---

## 📅 10일 커리큘럼

| Day | 주제 | 핵심 내용 | 코드 제공 여부 |
|-----|------|-----------|----------------|
| **Day 1** | RAG 파이프라인 최소 구조 | • 파이프라인 개념 이해<br>• main → pipeline → loader 흐름<br>• 3파일 구조로 RAG 뼈대 파악 | ✅ **제공** |
| **Day 2** | Python 문서 파이프라인 + Docker | • 파일 I/O (with open 패턴)<br>• config.yaml 분리<br>• 경로 처리 (BASE_DIR)<br>• Docker 빌드 & 실행 | ✅ **제공** |
| **Day 3** | FastAPI + 실무 Python | • FastAPI 서버 구축<br>• dataclass / Pydantic<br>• `/query` API<br>• Swagger UI (`/docs`) | ✅ **제공** |
| **Day 4** | 로컬 LLM 서빙 (CPU) + Docker | • 경량 모델 (GGUF)<br>• llama.cpp 사용<br>• CPU 추론<br>• Docker로 LLM 서빙 | ❌ **전자책 전용** |
| **Day 5** | Embedding & Vector DB | • SentenceTransformer<br>• FAISS 설치 및 사용<br>• Ingest (문서 색인)<br>• Top-K 검색 | ✅ **제공** |
| **Day 6** | Reranker & Hybrid Search | • Vector + Keyword Search<br>• BM25 Reranker<br>• Score Fusion<br>• Top-N 정렬 | ✅ **제공** |
| **Day 7** | Orchestration (3-Stage) | • 3단계 파이프라인<br>• step_retrieve()<br>• step_rerank()<br>• step_generate()<br>• Trace 객체 | ✅ **제공** |
| **Day 8** | LLM Gateway + 외부 API 연결 | • Gateway 패턴 구조 학습<br>• 외부 LLM API 연결 (OpenAI, Claude, Gemini)<br>• 로컬 CPU LLM 통합 (Day 4 모델 연동)<br>• Upstage Solar LLM (API 방식)<br>• API Key 기반 인증 설정<br>• router.py 라우팅 로직 (build_llm)<br>• Web UI 테스트 인터페이스<br>• Max Tokens/Temperature 파라미터 제어<br>• Gateway Status 실시간 확인 | ✅ **제공** |
| **Day 9** | Gateway + RAG 통합 | • Gateway에 RAG 파이프라인 연결<br>• 문서 검색 + 외부 LLM 생성<br>• Vector DB 실제 사용<br>• 모델별 비교 | ❌ **전자책 전용** |
| **Day 10** | 최종 통합 시스템 | • 전체 시스템 통합<br>• 외부 API + 로컬 모델 혼용<br>• 에이전트 패턴<br>• 오케스트레이션 고도화<br>• Vector DB 실전 활용 | ❌ **전자책 전용** |

**📌 Day 4, 9, 10은 전자책 구매 시 제공됩니다.**

---

## 🎯 주차별 학습 목표

### 🔹 1주차 (Day 1-3): Python 기초 + API 서버

**목표**: Python 구조화 코드 작성 + FastAPI 서버 구축

- Day 1: 구조 이해 ✅
- Day 2: 실무 코드 작성법 ✅
- Day 3: API 서비스화 ✅

**완료 상태**: ✅ FastAPI 서버로 질의 받기

---

### 🔹 2주차 전반 (Day 4-6): LLM + RAG 핵심

**목표**: 로컬 LLM + 검색 기반 생성

- Day 4: LLM 로딩 및 추론 ❌ (전자책)
- Day 5: 벡터 검색 (실제 Vector DB 사용) ✅
- Day 6: 검색 품질 향상 ✅

**완료 상태**: ✅ 문서 검색 → LLM 응답 생성

---

### 🔹 2주차 후반 (Day 7-10): 통합 + 외부 연결

**목표**: Gateway 패턴 + 외부 API 연결 + 전체 통합

- Day 7: 파이프라인 단계 분리 ✅
- Day 8: 외부 LLM API 실제 연결 (API Key 필요) ✅
- Day 9: Gateway + RAG + Vector DB 통합 ❌ (전자책)
- Day 10: 외부/로컬 혼용 완성형 시스템 ❌ (전자책)

**완료 상태**: ✅ 실제 동작하는 RAG 시스템 (구조 학습용)

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
- **Docker Desktop** (선택)
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
├─ README.md
├─ LICENSE
├─ .gitignore
│
├─ docs/                      # 📖 학습 자료
│  ├─ setup-guide.md          # 환경 설정 가이드
│  ├─ ebook-sample-1.md       # Day 1 샘플
│  ├─ ebook-sample-2.md       # Day 5 샘플  
│  └─ ebook-sample-3.md       # Day 8 샘플
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

- ❌ "AI 공부했다"
- ✅ **"RAG 하나 직접 만들었다"**
- ✅ Python 실무 코드 거부감 제거
- ✅ LLM/RAG 구조 완벽 이해
- ✅ SI·PoC·제안서 투입 가능

---
## 🔑 API Key 설정

### 1. 템플릿 파일 복사
```bash
cd gateway/secrets
cp api_keys.yaml.example api_keys.yaml
```

### 2. API Key 발급

각 서비스에서 API Key를 발급받으세요: Anthropic 은 키발급만 되고 토큰은 유료만 이용가능합니다.

- **OpenAI**: https://platform.openai.com/api-keys
- **Anthropic**: https://console.anthropic.com/settings/keys
- **Google AI**: https://aistudio.google.com/app/apikey
- **Upstage**: https://console.upstage.ai/api-keys

### 3. `api_keys.yaml` 편집

발급받은 키를 입력하세요:
```yaml
openai:
  api_key: "sk-proj-xxxxxxxxxxxxx"  # 실제 키 입력

anthropic:
  api_key: "sk-ant-xxxxxxxxxxxxx"  # 실제 키 입력
```

### 4. 확인
```bash
# 폴더와 파일을 생성해야 합니다. 로컬에서 만들어서 확인 필요
api_keys.yaml 을 별도로 만들어야 함.
위치 secrets/api_keys.yaml
현재 secrets/api_keys.yaml.example
```

### ⚠️ 주의사항

- ❌ `api_keys.yaml` 파일을 절대 Git에 커밋하지 마세요
- ✅ `api_keys.yaml.example`만 GitHub에 올립니다
- 🔒 실수로 키를 올렸다면 즉시 키를 재발급하세요



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

- **저자 블로그**: https://j4zlap.tistory.com
- **GitHub**: https://github.com/rechard0609
- **이메일**: j4angguiop@gmail.com

---

## 🔒 전자책 구매 안내

### 전자책에서만 제공되는 내용

- ✅ **Day 4**: 로컬 LLM 서빙 전체 구현
- ✅ **Day 9**: Gateway + RAG 완전 통합
- ✅ **Day 10**: Agent + Orchestration 고급 구현
- ✅ **모든 실습 예제 솔루션**
- ✅ **연습 문제 정답 및 해설**
- ✅ **케이스 스터디 전체 소스**
- ✅ **프로덕션 체크리스트**
- ✅ **트러블슈팅 가이드**

### 구매 문의

📧 **Email**: j4angguiop@gmail.com  
📝 **Blog**: https://j4zlap.tistory.com

---

## 📚 버전 히스토리 | Version History

- **v1.0** (2022.06): 초안 완성 | Initial version
- **v2.0** (2023.12): LLaMA 지원 | LLaMA support
- **v3.0** (2024.12): Gateway & Orchestration
- **v4.0** (2026.01): 최종 완성 | Final release

---

**⭐ 이 프로젝트가 도움이 되었다면 Star를 눌러주세요!**  
**⭐ If this project helps you, please give it a star!**

---

**Copyright © 2022-2026 정상혁 (Sanghyuk Jung). All Rights Reserved.**
