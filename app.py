# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import spacy

app = FastAPI()
nlp = spacy.load('en_core_web_md')

class TextRequest(BaseModel):
    statement: str
    sentences: list[str]

@app.post("/similarity")
async def similarity(request: TextRequest):
    statement_doc = nlp(request.statement)
    results = []
    for sentence in request.sentences:
        sentence_doc = nlp(sentence)
        similarity_score = statement_doc.similarity(sentence_doc)
        results.append({"sentence": sentence, "similarity": similarity_score})
    return {"statement": request.statement, "results": results}
