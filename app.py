import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter # , MarkdownTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import re
# import glob
import time

load_dotenv()

def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)

def update_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                content_no_emoji = remove_emojis(content)

                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content_no_emoji)
            except Exception as e:
                print(f"Error procesando {file_path}: {e}")

# Call update_files with the directory that contains your .md files to delete emojis, only need to do when preparing new Challenge documents
# update_files('E:\GitHub\groq-gemini\md')

# Load the GROQ And OpenAI API KEY
groq_api_key= st.secrets["GROQ_API_KEY"]
os.environ["GOOGLE_API_KEY"]= st.secrets["GOOGLE_API_KEY"]


st.title("Scaffold-ETH 2 Documents and SpeedRunEthereum Q&A")

# Groq available models:
# llama3-70b-8192
# llama3-8b-8192
# gemma-7b-it
# mixtral-8x7b-32768
# llama-3.3-70b-versatile (changing to this one since llama3-70b-8192 will be deprecated on 08/30)

llm=ChatGroq(groq_api_key=groq_api_key,
             model_name="llama-3.3-70b-versatile")

prompt=ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}

"""
)

# Add a selectbox to the sidebar.
challenge_dir = st.sidebar.selectbox(
    'Select a Challenge',
    ('Challenge 0',)
)


def vector_embedding():
    # Reset the vectors if they are already loaded
    if "vectors" in st.session_state:
        del st.session_state['vectors']

    if "vectors" not in st.session_state:
        # embedding all directory files
        print('Starting vector embedding...')
        st.session_state.embeddings=GoogleGenerativeAIEmbeddings(model = "models/embedding-001")

        st.session_state.loader=DirectoryLoader(f'{challenge_dir}', glob='**/*.*', show_progress=True, loader_cls=TextLoader)

        st.session_state.docs=st.session_state.loader.load() ## Document Loading

        # Show amount of documents to verify is working fine
        # st.text(len(st.session_state.docs) if len(st.session_state.docs) > 0 else None)

        # should try also MarkdownTextSplitter
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1200,chunk_overlap=128) ## Chunk Creation
        #st.session_state.text_splitter=MarkdownTextSplitter(chunk_size=1200,chunk_overlap=128) ## Chunk Creation

        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs[:20]) #splitting
        st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings) #vector embeddings

# Check if 'challenge_dir' is in session state
if 'challenge_dir' not in st.session_state:
    st.session_state['challenge_dir'] = challenge_dir  # Initialize it
    vector_embedding()  # Call vector_embedding() for the first time
elif st.session_state['challenge_dir'] != challenge_dir:
    st.session_state['challenge_dir'] = challenge_dir  # Update it
    vector_embedding()  # Call vector_embedding() when the challenge_dir changes

# Call vector_embedding() before trying to access "vectors"
# vector_embedding()
prompt1=st.text_input("Enter Your Question From the Challenge or Scaffold-ETH Documents")

import time

if prompt1:
    document_chain=create_stuff_documents_chain(llm,prompt)
    retriever=st.session_state.vectors.as_retriever()
    retrieval_chain=create_retrieval_chain(retriever,document_chain)
    start=time.process_time()
    response=retrieval_chain.invoke({'input':prompt1})
    print("Response time :",time.process_time()-start)
    st.write(response['answer'])

    # With a streamlit expander
    with st.expander("Document Similarity Search"):
        # Find the relevant chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")
