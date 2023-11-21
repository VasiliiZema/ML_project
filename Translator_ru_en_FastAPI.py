from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()

classifier = pipeline(model="Helsinki-NLP/opus-mt-ru-en")

# @app.get("/predict/")
# def predict():
#     return (f"Перевод на английский язык: {classifier('Привет, как дела Василий?')[0]['translation_text']}")

@app.post("/predict/")
def predict(item: Item):
    return f"Перевод на английский язык: {classifier(item.text)[0]['translation_text']}"

