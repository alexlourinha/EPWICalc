from fastapi import FastAPI

app = FastAPI()


@app.get("/character")
def get_character():
    return {"name": "Alejandro", "age": 25}


@app.post("/character")
def create_character(character: dict):
    print(character.values())
    return character
