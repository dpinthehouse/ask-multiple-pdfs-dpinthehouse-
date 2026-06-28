import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub
from langchain.docstore.document import Document

def get_pdf_documents(pdf_docs):
    documents = []

    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)

        for page_number, page in enumerate(pdf_reader.pages):
            text = page.extract_text()

            if text:
                documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "source": pdf.name,
                            "page": page_number + 1
                        }
                    )
                )

    return documents


def get_text_chunks(documents):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    chunked_documents = text_splitter.split_documents(documents)

    return chunked_documents


def get_vectorstore(chunked_documents):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")

    vectorstore = FAISS.from_documents(
        documents=chunked_documents,
        embedding=embeddings
    )

    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True,output_key="answer")
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
        memory=memory,
        return_source_documents=True
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    source_documents = response["source_documents"]
    
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(
                bot_template.replace("{{MSG}}", message.content),
                unsafe_allow_html=True
                )

            sources = {}

            for doc in source_documents:
              filename = doc.metadata["source"]
              page = doc.metadata["page"]

              if filename not in sources:
               sources[filename] = set()

              sources[filename].add(page)

            st.markdown("**Sources:**")

            for filename in sorted(sources.keys()):
               pages = sorted(sources[filename])

               if len(pages) == 1:
                 page_text = f"Page {pages[0]}"
               else:
                 page_text = "Pages " + ", ".join(str(page) for page in pages)
 
               st.write(f"• {filename} ({page_text})")
           


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs",
                       page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with multiple PDFs :books:")
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf documents
                documents = get_pdf_documents(pdf_docs)

                # get the document chunks
                chunked_documents = get_text_chunks(documents)

                # create vector store
                vectorstore = get_vectorstore(chunked_documents)

                # create conversation chain
                st.session_state.conversation = get_conversation_chain(
                    vectorstore)


if __name__ == '__main__':
    main()
