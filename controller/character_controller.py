from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service.calculator_service import calculate_character_stats


app = FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/character")
def get_character():
    return {"name": "Alejandro", "age": 25}


@app.post("/character")
def create_character(character: dict):
    result = calculate_character_stats(character)
    return result
