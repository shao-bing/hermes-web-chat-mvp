from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    import subprocess

    result = subprocess.run(
        ["hermes", "chat", "-Q", "-q", req.message],
        capture_output=True,
        text=True
    )

    print("RETURN CODE:", result.returncode)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    if result.returncode != 0:
        return {
            "reply": result.stderr.strip() or "Hermes CLI failed"
    }

    return {
        "reply": result.stdout.strip()
    }    
