# 환경 설정 가이드
> RAG-on-Local-CPU-minimal 시작을 위한 최소 환경 설정

---

## ⚠️ 중요 공지

**개인 환경의 다양한 변수로 인해 설치 가이드는 제공하지 않습니다.**  
각 소프트웨어의 **공식 문서**를 참고하여 설치하세요.

---

## 필수 소프트웨어

다음 3가지만 설치하면 시작할 수 있습니다:

- [ ] **Python 3.10+**
- [ ] **Git**
- [ ] **VS Code** (권장)

**선택 사항:**
- [ ] **Docker Desktop** (Day 2에서 사용)

---

## Python

### 권장 버전
```
Python 3.10 ~ 3.11
```

### 설치 확인
```bash
python --version
# Python 3.10.6
```

### 공식 문서
https://www.python.org/downloads/

---

## Git

### 설치 확인
```bash
git --version
# git version 2.40.0
```

### 공식 문서
https://git-scm.com/downloads

---

## VS Code (권장)

### 왜 VS Code인가?

**이 프로젝트에서는 VS Code를 강력히 권장합니다:**
- ✅ **터미널 통합**: 코드 작성 + 터미널 작업을 한 화면에서
- ✅ **디버깅 도구**: 브레이크포인트, 변수 확인 등 학습에 필수
- ✅ **이용도 증가**: Day 3부터 FastAPI, Docker 등 터미널 작업 급증
- ✅ **Python 지원**: 확장 프로그램으로 코드 자동완성, 린팅 지원

**대안**: PyCharm, Cursor 등 사용 가능하나, 실습 설명은 VS Code 기준

### 설치 확인
VS Code 실행 가능하면 OK

### 공식 문서
https://code.visualstudio.com/

### 추천 확장 프로그램
```
- Python (Microsoft)
- Docker (선택)
```

---

## Docker Desktop (선택)

**사용 시점**: Day 2 (Docker 빌드 실습)

### 설치 확인
```bash
docker --version
# Docker version 24.0.0
```

### 공식 문서
https://www.docker.com/products/docker-desktop/

---

## API Key 준비 (Day 8 이후)

### OpenAI 또는 Anthropic

Day 8부터 **외부 LLM API 연결** 실습이 있습니다.

**준비 사항:**
- OpenAI API Key (https://platform.openai.com/)
- 또는 Anthropic API Key (https://console.anthropic.com/)

**환경변수 설정:**
```bash
# Windows (PowerShell)
$env:OPENAI_API_KEY="sk-..."

# macOS/Linux
export OPENAI_API_KEY="sk-..."
```

---

## 설치 확인
```bash
python --version
git --version
code --version  # VS Code
```

위 명령어가 정상 실행되면 **준비 완료**입니다! 🎉

---

## 프로젝트 클론
```bash
git clone https://github.com/rechard0609/RAG-on-Local-CPU-minimal.git
cd RAG-on-Local-CPU-minimal

# VS Code로 열기
code .
```

---

## 문제 해결

### 공식 문서 우선 확인
- Python: https://docs.python.org/
- Git: https://git-scm.com/doc
- VS Code: https://code.visualstudio.com/docs
- Docker: https://docs.docker.com/

### 에러 발생 시
1. 에러 메시지 전체 복사
2. Google 검색
3. Stack Overflow 참고

---

## 다음 단계

설치가 완료되었다면:

**👉 [Day 1 시작하기](../Rag_minimal_day1/README.md)**

---

**Copyright © 2022 정상혁 (Sanghyuk Jung). All Rights Reserved.**  
**License**: CC BY-NC-ND 4.0