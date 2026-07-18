from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import chromadb
from chromadb.utils import embedding_functions

app = FastAPI()

# Подключаем Chroma
client = chromadb.PersistentClient(path="./chroma_db")
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection = client.get_collection(name="vacancies", embedding_function=sentence_transformer_ef)

class QueryRequest(BaseModel):
    query: str

@app.get("/")
async def get_ui():
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/api/search")
async def search_rag(req: QueryRequest):
    results = collection.query(
        query_texts=[req.query],
        n_results=3
    )
    
    # Собираем структурированные данные
    response_data = []
    for meta in results['metadatas'][0]:
        response_data.append({
            "title": meta['title'],
            "company": meta['company'],
            "id": meta['vacancy_id']
        })
        
    # Возвращаем JSON с ключом results
    return {"results": response_data}