import pandas as pd
import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import requests

df = joblib.load('embeddings.joblib')
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

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        # "model": "deepseek-r1",
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })

    response = r.json()
    print(response)
    return response

incoming_query = input("Ask a question: ")
question_embedding = create_embeddings([incoming_query])[0]
# print(question_embedding)

#Find similarities of Question Embeddings with other embeddings
similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()
# print(similarities)
top_results = 5
max_indx = similarities.argsort()[::-1][0:top_results]
# print(max_indx)
new_df = df.loc[max_indx] 
# print(new_df[["title", "number", "text"]])

prompt = f''' Here are video subtitle chunks containing video title, video number, start time in seconds, end time in seconds, the text at that time:

{new_df[["title", "number", "start", "end", "text"]].to_json(orient="records")}
---------------------------------
"{incoming_query}"
User asked this question related to the video chunks, you have to answer in a human way (dont mention the above format, its just for you) where and how much content is taught in which video (in which video and at what timestamp) and guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer questions related to the course
'''
with open("prompt.txt", "w") as f:
    f.write(prompt)

response = inference(prompt)["response"]
print(response)

with open("response.txt", "w") as f:
    f.write(response)
# for index , item in new_df.iterrows():
#     print(index ,item["number"],item["title"],item["text"], item["start"], item["end"])