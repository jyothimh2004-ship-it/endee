# AI Resume Semantic Search using Endee

## Project Overview
This project demonstrates an AI/ML application using the Endee vector database.  
The system performs semantic search on resume data. Instead of matching exact keywords, it understands the meaning of a search query and returns the most relevant resume.

This project shows how vector databases can be used in modern AI applications such as semantic search, recommendation systems, and Retrieval Augmented Generation (RAG).

## Objective
The goal of this project is to build a simple AI-powered resume search system where:
- Resume text is converted into embeddings (vectors)
- Vectors are stored in a vector database
- A user query is also converted to a vector
- The system finds the most similar resume using vector similarity

## Technologies Used
- Python
- Sentence Transformers
- NumPy
- Endee Vector Database
- GitHub

## System Design
The system follows these steps:

1. Load resume data
2. Convert text data into vector embeddings using an embedding model
3. Store the vectors in the vector database
4. Convert the user search query into a vector
5. Perform similarity search
6. Return the most relevant result

Flow:

User Query → Embedding Model → Vector Search → Best Matching Resume

## How Endee is Used
Endee is used as the base vector database repository.  
The project is built on top of the forked Endee repository to demonstrate how vector storage and similarity search can support AI applications.

The vector database stores embeddings generated from resume text and allows efficient similarity-based retrieval.

## Features
- Semantic search
- AI text embeddings
- Vector similarity search
- Simple command line interface
- Demonstration of vector database usage

## Future Improvements
- Upload and index real resumes (PDF/DOCX)
- Build a web interface
- Add RAG-based chatbot
- Use a larger dataset
- Integrate APIs for real-time applications

## Conclusion
This project demonstrates how vector databases can power AI-driven search systems.  
By combining embeddings with vector similarity search, the system can understand user queries and return meaningful results beyond simple keyword matching.
