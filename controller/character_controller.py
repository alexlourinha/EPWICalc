from fastapi import FastAPI

from service.calculator_service import calculate_character_stats


app = FastAPI()


@app.get("/character")
def get_character():
    return {"name": "Alejandro", "age": 25}


@app.post("/character")
def create_character(character: dict):
    result = calculate_character_stats(character)
    return result
