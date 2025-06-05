from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    name: str
    goal: str

@app.post("/generate-programme")
def generate_programme(data: UserInput):
    # Placeholder logic
    return {
        "message": f"Programme generated for {data.name} with goal: {data.goal}"
    }
