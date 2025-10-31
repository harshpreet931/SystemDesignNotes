import torch
import chromadb # Vectordb
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForCausalLM, AutoTokenizer

# Part 1 - Init
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client()
collection = client.create_collection("xyz")

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-0.6B") # Local-llms 
llm = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen3-0.6B",
    dtype=torch.float32, 
    device_map="cpu"
)

# Part 2 - Documents
documents = [
    "Harsh likes ice cream.",
    "Harsh likes mint chocolate chip ice cream.",
    "Harsh likes system design."
]

embeddings = embedding_model.encode(documents)
collection.add(
    embeddings=embeddings.tolist(),
    documents=documents,
    ids=["doc1", "doc2", "doc3"]
)

question = "What does Harsh like? Explain in detail."
print(f"\nQuestion: {question}")

query_embedding = embedding_model.encode([question])

results = collection.query(
    query_embeddings=query_embedding.tolist(),
    n_results=2
)

context = "\n".join(results['documents'][0])
print("\nRetrieved Context:")
print(context)


prompt_template = f"""Answer this question using the provided context.

Context:
{context}

Question: {question}

Provide a clear, concise answer:"""

text = tokenizer.apply_chat_template(
    [
        {"role": "user", "content": prompt_template}
    ], 
    tokenize=False, 
    add_generation_prompt=True
) 

model_inputs = tokenizer([text], return_tensors="pt").to(llm.device)

generated_ids = llm.generate(
    **model_inputs,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.8,
    top_k=20
)

response_ids = generated_ids[0][len(model_inputs.input_ids[0]):]
answer = tokenizer.decode(response_ids, skip_special_tokens=True)

print("\nRAG Answer:")
print(answer.strip())

client.delete_collection("xyz")