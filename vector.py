from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd


import os

for f in os.listdir("archive"):
    if f.endswith(".csv"):
        print(f)


df = pd.read_csv("archive/power_plant_database_global.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_lagchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i , row in df.interrows():
        document = Document(
            page_content=row["review"],
            metadata={"source": f}) , id=str(i)
        
        
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="power_plant_database_global",
    persist_directory=db_location,
    embedding_function=embeddings

)


if add_documents:
    vector_store.add_documents(documents = documents, ids = ids)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)








