from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

docs = [
"Python developer with ML experience",
"Java developer with Spring Boot",
"Data scientist with AI skills",
"Web developer with React",
"Machine learning engineer",
"AI chatbot developer"
]

vectors = model.encode(docs)

print("Resume database loaded")

def search(query):
    q_vec = model.encode([query])[0]
    scores = np.dot(vectors, q_vec)
    best = np.argmax(scores)
    print("Best match:", docs[best])

while True:
    q = input("Search resume: ")

    if q == "exit":
        break

    search(q)
