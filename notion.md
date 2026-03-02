# 🤖 바이브코딩 스터디 기록 - Persona-AI

### 1. 이번 주 활동 한 줄 요약
교육용 AI 대화 서비스 'Persona-AI'의 Web MVP 구축 및 클라우드 배포(Render.com) 완료.

### 2. 프로젝트 핵심 내용
- **Thin-Client 아키텍처:** FastAPI(백엔드)와 Vanilla JS(프론트엔드)를 결합하여 저사양 기기에서도 원활한 AI 대화가 가능한 구조 설계.
- **안전한 교육 환경:** '마스터 프롬프트'를 통한 유해 콘텐츠 차단 및 '유저 페르소나' 설정을 통한 맞춤형 대화 경험 제공.

### 3. 재현 가능 가이드
- **실행 단계:**
  1. `.env` 파일에 `GOOGLE_API_KEY` 설정.
  2. `pip install -r requirements.txt`로 의존성 설치.
  3. `python app.py` 실행 후 `localhost:8000` 접속.
- **핵심 코드:** `app.py` 내 `models/gemini-flash-latest` 모델을 사용한 대화 세션 관리 로직.

### 4. 다음 주 목표 (Action Item)
- [ ] 브라우저 Web Speech API를 활용한 음성 상호작용(STT/TTS) 구현.
- [ ] 답변 생성 시 실시간 스트리밍(Streaming) 응답 UI 적용.
