from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.markdown import UnstructuredMarkdownLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# Let's load the markdown document
md_loader = UnstructuredMarkdownLoader(file_path='data/Potter 3000 Whasing Machine User Manual.md')
document = md_loader.load()

# Let's make some chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
chunked_document = splitter.split_documents(document)

# Vectorize chunks into Chroma
chromadb = Chroma.from_documents(documents=chunked_document, embedding=OllamaEmbeddings(model='llama2'), persist_directory='.chromadb')