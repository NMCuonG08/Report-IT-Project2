from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import textwrap

# Load PDFs from the directory
loader = PyPDFDirectoryLoader("new-data")
pdf_docs = loader.load()

# Prepare the list of documents with metadata
docs = []
for doc in pdf_docs:
    if 'page_number' not in doc.metadata:
        doc.metadata['page_number'] = doc.metadata.get('page', 'Unknown')
    doc.metadata['file_name'] = doc.metadata.get('source', 'Unknown')
    docs.append(doc)

# Initialize Chroma Vector Store with embeddings
embedding_model = OllamaEmbeddings(model="qwen2")
vector_store = Chroma.from_documents(
    documents=docs,
    collection_name="ollama_embeds",
    embedding=embedding_model
)

# Use the retriever to get relevant documents
retriever = vector_store.as_retriever()
query = "Quy chế đào tạo Trường Đại học Sư phạm Kỹ thuật TP. Hồ Chí Minh"
retrieved_docs = retriever.get_relevant_documents(query)

# Calculate and display Cosine Similarity
query_embedding = embedding_model.embed_query(query)  # Get the query embedding

for result in retrieved_docs:
    # Get the document embedding
    doc_embedding = embedding_model.embed_query(result.page_content)  # Use the content to get the embedding
    similarity_score = cosine_similarity([query_embedding], [doc_embedding])[0][0]

    page_number = result.metadata.get('page_number', 'Unknown')
    file_name = result.metadata.get('file_name', 'Unknown')

    # Display the document with the similarity score
    print("\n" + "=" * 50)
    print(f"Tài liệu: {file_name} (Trang: {page_number + 1})")
    print(f"Cosine Similarity: {similarity_score:.4f}")
    print("=" * 50)
    print(f"Nội dung: \n{textwrap.fill(result.page_content[:200], width=100)}...\n")
