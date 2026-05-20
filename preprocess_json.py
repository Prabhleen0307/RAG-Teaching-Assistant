import requests
import os
import json
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity

# ---- embedding function (batch-style, but Ollama-safe) ----
def create_embeddings(text_list):
    embeddings = []

    for text in text_list:
        r = requests.post(
            "http://localhost:11434/api/embeddings",
            json={
                "model": "bge-m3",
                "prompt": text
            }
        )
        embeddings.append(r.json()["embedding"])

    return embeddings


# ---- read all json files ----
jsons = os.listdir("jsons")

chunk_id = 0
my_dicts = []

for json_file in jsons:
    with open(f"jsons/{json_file}", "r", encoding="utf-8") as f:
        content = json.load(f)
        print(f"Creating Embeddings for {json_file}")
    # collect texts first (your original intent)
    text_list = [c["text"] for c in content["chunks"]]

    # create embeddings for this file’s chunks
    embeddings = create_embeddings(text_list)

    # map embeddings back to chunks (index-based)
    for i, chunk in enumerate(content["chunks"]):
        chunk["chunk_id"] = chunk_id
        chunk["embedding"] = embeddings[i]   # ✅ vector, not text
        chunk_id += 1
        my_dicts.append(chunk)
# print("Total chunks embedded:", len(my_dicts))

df = pd.DataFrame.from_records(my_dicts) # u give it a list of dictionaries u get a data frame 

#save this data frame 
joblib.dump(df, "embeddings.joblib")
print("✅ embeddings.joblib saved successfully")
print(df.head())



