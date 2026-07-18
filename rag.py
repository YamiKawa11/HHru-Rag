import json
import chromadb
from chromadb.utils import embedding_functions

def build_vector_db(json_filepath, db_path="./chroma_db"):
    client = chromadb.PersistentClient(path=db_path)

    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    collection = client.get_or_create_collection(
        name="vacancies",
        embedding_function=sentence_transformer_ef
    )

    with open(json_filepath, 'r', encoding='utf-8') as f:
        docs = json.load(f)

    documents = []
    metadatas = []
    ids = []

    for idx, doc in enumerate(docs):
        documents.append(doc["page_content"])
        metadatas.append(doc["metadata"])
        ids.append(str(doc["metadata"]["vacancy_id"]))

    print(f"Чтение завершено. Найдено {len(documents)} записей.")
    print("Начало векторизации...")
    
    batch_size = 100
    for i in range(0, len(documents), batch_size):
        end_idx = min(i + batch_size, len(documents))
        
        collection.add(
            documents=documents[i:end_idx],
            metadatas=metadatas[i:end_idx],
            ids=ids[i:end_idx]
        )
        print(f"Добавлено в индекс: {end_idx}/{len(documents)}")

    print("Индексация завершена. База сохранена локально.\n")

    test_query = "подработка на пару часов, багфикс и легаси"
    print(f"Тестовый запрос: '{test_query}'")
    
    results = collection.query(
        query_texts=[test_query],
        n_results=2,
    )

    print("Результаты:")
    for i, meta in enumerate(results['metadatas'][0]):
        distance = round(results['distances'][0][i], 3)
        print(f"{i+1}. {meta['company']} — {meta['title']} (distance: {distance})")

if __name__ == "__main__":
    build_vector_db('rag_documents.json')