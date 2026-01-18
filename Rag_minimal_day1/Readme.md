# Day 1: RAG 파이프라인 최소 구조

> **GitHub Repository**: [RAG-on-Local-CPU-minimal](https://github.com/rechard0609/RAG-on-Local-CPU-minimal)

> 3파일로 이해하는 RAG의 뼈대

---

## 🎯 학습 목표

Day 1의 핵심은 다음 한 문장입니다:

> **RAG는 복잡한 기술이 아니라 단계적으로 연결된 파이프라인이다.**

이 Day를 마치면:
- ✅ `main → pipeline → loader` 흐름 이해
- ✅ RAG 파이프라인의 기본 구조 파악
- ✅ Python 모듈 분리의 기본 이해

---

## 📂 프로젝트 구조

```
Rag_minimal_day1/
├── main.py          # 진입점 (시작)
├── pipeline.py      # RAG 파이프라인 (흐름)
└── loader.py        # 문서 로더 (데이터)
```

---

## 🔄 실행 흐름도

```
┌──────────────┐
│   main.py    │  1. 프로그램 시작
│   (시작점)    │     query 정의
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ pipeline.py  │  2. RAG 파이프라인 실행
│ (파이프라인)  │     각 단계 연결
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  loader.py   │  3. 문서 로딩
│ (문서 로더)   │     문서 목록 반환
└──────┬───────┘
       │
       ▼
    문서 반환
       │
       ▼
  pipeline 결과
       │
       ▼
    화면 출력
```

---

## ⚙️ VS Code에서 실행하기

### 1. VS Code 열기

**Windows 사용자 (PowerShell):**
```powershell
cd Rag_minimal_day1
code .
```

**macOS/Linux 사용자 (Bash):**
```bash
cd Rag_minimal_day1
code .
```

### 2. Python 파일 실행

**방법 1: PowerShell/Bash 사용**

Windows (PowerShell):
```powershell
python main.py
```

macOS/Linux (Bash):
```bash
python main.py
# 또는
python3 main.py
```

**방법 2: VS Code 실행 버튼**
- `main.py` 파일 열기
- 우측 상단 ▶️ 버튼 클릭 (OS 무관)

**예상 출력:**
```
=== QUERY ===
RAG가 뭐야?

=== DOCUMENTS ===
- (1) RAG 개념: RAG는 Retrieval Augmented Generation의 약자이다.
- (2) LLM 개념: LLM은 대규모 언어 모델을 문맥을 기반으로 답변한다.
- (3) Pipeline: AI 시스템은 단계별 파이프라인으로 구성된다.
```

---

## 🐛 디버깅 방법

### 사전 준비

**VS Code Python 확장 설치 (필수)**
1. VS Code 열기
2. 왼쪽 확장 아이콘 클릭 (또는 `Ctrl + Shift + X`)
3. "Python" 검색
4. Microsoft의 Python 확장 설치

### 방법 1: print() 사용

**loader.py에 디버깅 추가:**
```python
def load_documents():
    print("📂 문서 로딩 시작")  # 디버깅용
    docs = ["doc1.txt", "doc2.txt", "doc3.txt"]
    print(f"✅ {len(docs)}개 로딩 완료")  # 결과 확인
    return docs
```

**실행 결과:**
```
📂 문서 로딩 시작
✅ 3개 로딩 완료
=== QUERY ===
RAG가 뭐야?
...
```

### 방법 2: VS Code 디버거 사용

**1. 브레이크포인트 설정**
- `main.py` 파일 열기
- 7번 줄 (print 문) 왼쪽 클릭 → 빨간 점 생성
- 원하는 만큼 여러 줄에 설정 가능

**2. 디버그 실행**
- **F5** 누르기
- "Python Debugger" 선택 (처음 한 번만)
- 브레이크포인트에서 코드가 멈춤 (노란색 배경)

**3. 디버그 컨트롤**
- **F5**: 다음 브레이크포인트까지 실행 (Continue)
- **F10**: 다음 줄로 이동 (Step Over)
- **F11**: 함수 안으로 들어가기 (Step Into)
- **Shift + F11**: 함수에서 나오기 (Step Out)

**4. 변수 확인**
- **왼쪽 패널 "VARIABLES"**: 모든 변수 값 확인
  - Locals: query, result 등
- **변수 위에 마우스 오버**: 값 미리보기
- **WATCH 패널**: 특정 변수 추적 가능

**5. 디버그 화면 구성**
```
왼쪽 패널:
├─ VARIABLES    # 현재 변수들
├─ WATCH        # 감시할 변수 추가
├─ CALL STACK   # 함수 호출 순서
└─ BREAKPOINTS  # 브레이크포인트 목록

하단:
└─ Python Debug Console  # 디버그 중 명령 실행
```

**디버깅 팁:**
```
main.py:7 에서 시작 (print 문)
  ↓ F11 (Step Into)
pipeline.py 진입
  ↓ F11 (Step Into)
loader.py 진입
  ↓ 왼쪽 VARIABLES에서 docs 확인
  ↓ F10 (Step Over)
반환값 확인
```

---

## 🧠 파일별 역할

### main.py
```python
# 역할: 프로그램 시작점
# - 사용자 쿼리 정의
# - pipeline 호출
# - 결과 출력
```

**핵심 코드:**
- `query = "RAG가 뭐야?"` - 사용자 질문
- `result = pipeline(query)` - 파이프라인 실행
- `print(result)` - 결과 출력

### pipeline.py
```python
# 역할: RAG 파이프라인 중심
# - 여러 단계를 연결하는 허브
# - Day 2부터 단계가 계속 추가됨
# - 현재: loader만 호출
```

**핵심 개념:**
- 파이프라인은 "단계들의 연결"
- 현재는 단순하지만, 앞으로 복잡해짐
- Retrieve → Rerank → Generate 등 추가 예정

### loader.py
```python
# 역할: 문서 가져오기
# - Day 1: 하드코딩된 문서 목록
# - 향후: 파일 / DB / API로 교체 가능
```

**현재 구현:**
- 3개의 고정된 문서 반환
- Day 2부터 실제 파일 읽기로 변경

---

## ✅ Day 1 완료 기준

다음을 이해했다면 완료입니다:

- ✔️ `main → pipeline → loader` 흐름을 설명할 수 있다
- ✔️ RAG가 "단계적 파이프라인"임을 이해했다
- ✔️ VS Code에서 코드를 실행할 수 있다
- ✔️ 브레이크포인트로 디버깅할 수 있다
- ✔️ pipeline에 단계가 추가될 수 있음을 인지했다

---

## 🔜 다음 단계 (Day 2)

Day 2에서는 다음을 추가합니다:

- ✅ 실제 파일에서 문서 읽기 (`data/docs.txt`)
- ✅ `config.yaml`로 설정 분리
- ✅ Docker 컨테이너로 실행 환경 구축
- ✅ 경로 처리 (`BASE_DIR` 패턴)

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