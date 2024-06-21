from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain.chains import retrieval_qa
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from argparse import ArgumentParser

# Constants
MESSAGE_WITH_CONTEXT = """
Answer this question using the provided context only as best as you can.

{question}

Context:
{context}
"""
MESSAGE_WITHOUT_CONTEXT = """
Answer this question as best as you can.

{question}
"""

# Define LLM
llm = ChatGroq(model="llama3-8b-8192",api_key='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')

# Get args
parser = ArgumentParser()
parser.add_argument("--context", action='store_true')
parser.add_argument("--question", type=str, required=True)
args = parser.parse_args()

if args.context:
    # Open Chroma
    chromadb = Chroma(persist_directory='.chromadb',embedding_function=OllamaEmbeddings(model='llama2'))

    # Get retriever
    retriever = chromadb.as_retriever()
    prompt = ChatPromptTemplate.from_messages([("human", MESSAGE_WITH_CONTEXT)])
    rag_chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm
else:
    prompt = ChatPromptTemplate.from_messages([("human", MESSAGE_WITHOUT_CONTEXT)])
    rag_chain = {"question": RunnablePassthrough()} | prompt | llm

# Invoke chain
result = rag_chain.invoke(args.question)

print(result.content)