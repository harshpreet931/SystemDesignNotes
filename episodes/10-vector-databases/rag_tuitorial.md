# Mini RAG Tutorial

A simple introduction to Retrieval-Augmented Generation (RAG) using only local models.

## Installation

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python3.11 mini_rag.py
```

## What is RAG?

RAG combines two steps:
1. **Retrieval** - Find relevant documents using semantic search
2. **Generation** - Use an LLM to answer questions based on retrieved context

## How It Works

1. Store documents as vectors in a database
2. Convert questions to vectors
3. Find similar documents
4. Generate answers using retrieved context

## Models Used

- **Embedding**: all-MiniLM-L6-v2
- **Generation**: Qwen3-0.6B

Both models run locally on your machine.

## Example Output

```
Question: What does Harsh like and which one does he like?

Retrieved Context:
Harsh likes ice cream.
Harsh likes mint chocolate chip ice cream.

Answer:
Harsh likes ice cream, and he likes mint chocolate chip ice cream.
```

## Customize

- Add your own documents in the `documents` list
- Adjust `n_results` to retrieve more/fewer documents
- Modify the prompt in the `messages` section