# 📝 Project: Persona-AI Clicker 개발 기록

**날짜:** 2026-02-24 (Tuesday)
**작업 요약:** Web MVP 기초 구축, Gemini API 연동 및 Render.com 서버 배포 완료

## 1. 🚀 진행 작업 명세 (Gemini CLI 세션)
*   **프로젝트 구조 설계:** FastAPI(백엔드)와 Vanilla JS(프론트엔드)를 결합한 Thin-Client 구조 기반 마련.
*   **환경 설정:** Mac 환경을 고려한 `requirements.txt` 및 가상환경(venv) 가이드 작성.
*   **보안 설정:** `.gitignore`를 통해 API 키 및 불필요한 파일의 GitHub 유출 방지.
*   **배포 최적화:** Render.com 배포를 위한 동적 포트(PORT) 설정 및 Start Command 구성.
*   **Git 워크플로우:** GitHub 저장소 생성, 리모트 연결 및 지속적인 코드 푸시(Push) 수행.

## 2. 🛠 주요 에러 및 해결 과정 (Troubleshooting)

### ① f-string 멀티라인 문법 오류 (SyntaxError)
*   **문제:** `app.py`에서 `system_instruction` 및 `full_prompt` 작성 시 일반 f-string(`f"..."`) 내 줄바꿈으로 인한 문법 에러 발생.
*   **해결:** 파이썬의 삼중 따옴표 f-string(`f"""..."""`)을 도입하여 가독성과 문법 안정성 확보.

### ② 정적 파일/템플릿 경로 인식 실패
*   **문제:** 로컬에서는 `Persona-AI/static` 경로가 작동했으나, Render 배포 시 루트 디렉토리 기준 차이로 404 에러 발생.
*   **해결:** `app.py` 내 경로 설정을 상대 경로인 `static`, `templates`로 수정하여 배포 환경 호환성 해결.

### ③ Gemini 모델명 404 및 할당량 문제 (Critical)
*   **문제 1:** `models/gemini-1.5-flash` 인식 불가 (NotFound 404).
*   **문제 2:** `models/gemini-2.0-flash` 시도 시 할당량 초과(429 Resource Exhausted) 발생.
*   **디버깅:** `/check` 엔드포인트를 신설하고 `genai.list_models()`를 로그에 출력하여 실제 사용 가능한 모델 명칭 확인.
*   **해결:** 가장 안정적이고 할당량이 넉넉한 **`models/gemini-flash-latest`**로 모델명 확정 후 대화 성공.

### ④ 서버 로그 디버깅 강화
*   **문제:** Render에서 발생한 500 에러의 원인을 파악하기 어려움.
*   **해결:** `app.py` 내 `traceback.print_exc()`를 추가하여 Render 로그 탭에서 파이썬 에러의 원인(Traceback)을 즉시 확인할 수 있도록 개선.

## 3. ✅ 현재 상태 (Current Status)
*   **URL:** `https://persona-ai-sa01.onrender.com` (또는 설정된 Render URL)
*   **기능:** 페르소나 선택 기능, 대화 히스토리 유지, 실시간 채팅 UI 정상 작동.
*   **안전성:** 마스터 프롬프트가 적용되어 기본적으로 안전한 교육용 대화 환경 유지.

---

## 4. 📅 다음 작업 계획 (Next Session Plan)

### ① 프롬프트 엔지니어링 고도화 (핵심)
*   **Master Prompt 강화:** 미성년자 보호 로직을 더 엄격히 정의하고, 교육적 가이드라인(질문 유도형 대화) 반영.
*   **Persona별 System Instruction 세분화:** 현재 `index.html`에 있는 페르소나 리스트를 백엔드에서 더 정교한 말투(Persona Prompt)로 처리하도록 개선.

### ② UX/UI 및 편의 기능 추가
*   **음성 상호작용 (STT/TTS):** 브라우저 Web Speech API를 활용해 아이들이 목소리로 대화하고 들을 수 있는 기능 구현.
*   **스트리밍(Streaming) 응답:** AI의 답변이 생성되는 대로 실시간으로 화면에 뿌려주는 로직 추가.
*   **필러 사운드(Filler Sound):** 답변 대기 중 "음~", "어디 보자..." 같은 텍스트나 사운드 삽입 시도.

### ④ 지속 가능성 및 확장성
*   **커스텀 페르소나:** 템플릿 외에 학생이 직접 페르소나의 이름과 성격을 설정하는 기능.
*   **보호자 관리 모드:** 대화 요약본 확인 또는 마스터 설정 변경 페이지(MVP 이후 고려).

---

## 5. 🔄 Parallel Development: Persona-AI Gradio (2026-02-26)
*   **목적**: 빠른 기능 실험(음성 인식 등) 및 관리자용 프로토타이핑을 위해 Gradio 버전 병행 운영.
*   **진행 사항**:
    - `app_gradio.py` 구축 및 Gemini API `start_chat`을 이용한 히스토리 유지 로직 완성.
    - `PROJECT_CONTEXT_MAP.md`를 통해 FastAPI 버전과 Gradio 버전의 프롬프트 및 로직 동기화 관리.
    - 시각적 일관성을 위해 원본 앱의 Blue 테마와 Pretendard 폰트 스타일 계승.

---
**기록자:** Gemini CLI & User
**최종 업데이트:** 2026-02-26
