import pandas as pd
from pathlib import Path
import chromadb
from dotenv import load_dotenv
from groq import Groq

load_dotenv()





faqs_path = Path(__file__).parent/"/resources/faq_data.csv"
chroma_client = chromadb.Client()
collection_name_faq='faqs'

Groq_client = Groq()


def ingest_faq_data(path):
    if collection_name_faq not in [c.name for c in chroma_client.list_collections()]:
        print("ingesting faq Data into chroma db")
        collection = chroma_client.get_or_create_collection(
            name=collection_name_faq,
            
        )
        df = pd.read_csv(path)
        docs = df['question'].to_list()
        metadata = [{'answer': ans} for ans in df['answer'].to_list()]
        ids = [f"id_{i}" for i in range(len(docs))]
        collection.add(
            documents=docs,
            metadatas=metadata,
            ids=ids
        )
    else:
        print(f"Collection {collection_name_faq} already exists")
    

def get_relevant_qa(query):
    collection = chroma_client.get_collection(name=collection_name_faq)
    result = collection.query(
        query_texts=[query],
        n_results=2
    )
    return result

if __name__ == "__main__":
    ingest_faq_data(faqs_path)