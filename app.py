import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import json

load_dotenv()

app = FastAPI()

# static files and templates setup
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Configure Gemini API
# Make sure to set your GEMINI_API_KEY in the environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    # Fallback or error - in a real app, handle this securely
    print("Warning: GEMINI_API_KEY not found in environment variables.")
else:
    genai.configure(api_key=api_key)

# 기존 모델 선언 부분을 아래와 같이 수정해서 로그를 확인합니다.
try:
    # 현재 사용 가능한 모델 목록을 로그에 출력합니다.
    print("--- 사용 가능한 모델 목록 ---")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"사용 가능 모델: {m.name}")
    print("---------------------------")
except Exception as e:
    print(f"모델 목록 확인 실패: {e}")

# 일단 가장 최신 명칭인 1.5 Flash를 다시 시도하되, 'models/'를 붙여봅니다.
model = genai.GenerativeModel('models/gemini-2.0-flash')

# Master Prompt: Safety and Education Guidelines
MASTER_PROMPT = """
You are a safe, educational AI assistant for elementary school students. 
Rules:
1. Always be polite, encouraging, and patient.
2. Use simple language appropriate for children.
3. Strictly avoid any harmful, inappropriate, or adult content.
4. If asked about dangerous activities, gently redirect to a safe topic.
5. Focus on being a helpful companion and teacher.
"""

class ChatRequest(BaseModel):
    message: str
    persona: str
    history: list = []

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/check")
async def check_models():
    try:
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        return {"status": "success", "available_models": models}
    except Exception as e:
        return {"status": "error", "message": str(e)}
        
@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Combine Master Prompt + User Persona
        system_instruction = f"""{MASTER_PROMPT}

Your current persona is: {request.persona}
Act according to this persona while maintaining safety rules."""
        
        # In a real streaming scenario, we'd use model.generate_content(..., stream=True)
        # For simplicity in this MVP, we'll do a standard response first or a simple generator.
        
        chat_session = model.start_chat(history=request.history)
        
        # Prepend the system instruction as context if it's a new chat or every time
        full_prompt = f"""[System Context: {system_instruction}]
User: {request.message}"""
        
        response = chat_session.send_message(full_prompt)
        
        return {"response": response.text}
    except Exception as e:
        import traceback
        print(f"Error occurred: {str(e)}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
