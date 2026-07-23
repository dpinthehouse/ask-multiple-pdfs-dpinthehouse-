import time
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

    st.write(f"Creating embeddings for {len(chunked_documents)} chunks...")

    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.from_documents(
        documents=chunked_documents,
        embedding=embeddings
    )

    st.write("Embeddings complete!")

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

def highlight_answer_words(snippet, answer):
    stop_words = {
        "the", "a", "an", "is", "are", "was", "were",
        "at", "in", "on", "of", "to", "for", "and",
        "or", "with", "by"
    }

    words = answer.split()

    for word in words:
        clean_word = word.strip(".,!?()[]{}:;'\"").lower()

        if len(clean_word) < 4:
            continue

        if clean_word in stop_words:
            continue

        original_word = word.strip(".,!?()[]{}:;'\"")

        snippet = snippet.replace(
            original_word,
            f"**{original_word}**"
        )

    return snippet


def handle_userinput(user_question):
    start_time = time.time()

    response = st.session_state.conversation({'question': user_question})

    end_time = time.time()
    response_time = end_time - start_time
    answer = response["answer"]

    st.session_state.chat_history = response["chat_history"]
    source_documents = response["source_documents"]
    print("\n========== SOURCE DOCUMENTS ==========")

    for i, doc in enumerate(source_documents):
      print(f"\nDocument {i+1}")
      print("Metadata:", doc.metadata)
      print("Preview:", doc.page_content[:100])

    print("=====================================\n")

    num_sources = len(source_documents)

    # Display chat history
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(
                user_template.replace("{{MSG}}", message.content),
                unsafe_allow_html=True
            )
        else:
            st.write(
                bot_template.replace("{{MSG}}", message.content),
                unsafe_allow_html=True
            )
    
    st.info(f"⚡ Answer generated in {response_time:.2f} seconds")

    st.success(f"✓ Answer supported by {num_sources} document excerpts")
    # Display grouped evidence
    st.markdown("### Sources")

    grouped_sources = {}

    for doc in source_documents:
        filename = doc.metadata.get("source", "Unknown Source")
        page = doc.metadata.get("page", "Unknown Page")

        snippet = doc.page_content[:180]

        if len(doc.page_content) > 180:
            snippet += "..."

        snippet = highlight_answer_words(snippet, answer)    

        key = (filename, page)

        if key not in grouped_sources:
            grouped_sources[key] = []

        # Prevent duplicate snippets
        if snippet not in grouped_sources[key]:
            grouped_sources[key].append(snippet)

    labels = [
    "🥇 Most Relevant",
    "🥈 Relevant",
    "🥉 Additional Context"
]
    # Display grouped results
    for index, ((filename, page), snippets) in enumerate(grouped_sources.items()): 
     
     if index < len(labels):
        relevance = labels[index]
     else:
        relevance = "📄 Supporting Evidence"
        
     with st.expander(f"{relevance} • {filename} (Page {page})"):
        for snippet in snippets:
            st.markdown(snippet)
           


def main():
    load_dotenv()

    st.set_page_config(
        page_title="Chat with multiple PDFs",
        page_icon=":books:"
    )

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    if "document_info" not in st.session_state:
        st.session_state.document_info = []    

    st.header("Chat with multiple PDFs :books:")

    user_question = st.text_input("Ask a question about your documents:")

    if user_question:

        if st.session_state.conversation is None:
           st.warning("Please process at least one document first.")
        else:
           handle_userinput(user_question)

    with st.sidebar:

        st.subheader("Your documents")

        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'",
            accept_multiple_files=True
        )

        selected_documents = []

        if pdf_docs:

            st.markdown("### Select documents to search")

            col1, col2 = st.columns(2)

            if col1.button("Select All"):
                for pdf in pdf_docs:
                    st.session_state[f"doc_{pdf.name}"] = True

            if col2.button("Deselect All"):
                for pdf in pdf_docs:
                    st.session_state[f"doc_{pdf.name}"] = False

            for pdf in pdf_docs:

                key = f"doc_{pdf.name}"

                if key not in st.session_state:
                    st.session_state[key] = True

                if st.checkbox(pdf.name, key=key):
                    selected_documents.append(pdf)

        total_docs = len(pdf_docs) if pdf_docs else 0

        st.caption(
            f"Selected {len(selected_documents)} of {total_docs} document(s)"
        )

        process_clicked = st.button(
            "Process",
            disabled=not pdf_docs
        )

        if process_clicked:

            if not selected_documents:
                st.warning("Please select at least one document.")
                st.stop()

            with st.spinner("Processing"):

                st.write("Step 1: Reading PDFs...")

                documents = get_pdf_documents(selected_documents)

                num_pdfs = len(selected_documents)
                num_pages = len(documents)

                st.session_state.document_info = []

                for pdf in selected_documents:

                  pdf.seek(0)

                  reader = PdfReader(pdf)

                  st.session_state.document_info.append({
                    "name": pdf.name,
                    "pages": len(reader.pages)
                  })

                  pdf.seek(0)

                st.write("Step 2: Splitting text...")

                chunked_documents = get_text_chunks(documents)

                num_chunks = len(chunked_documents)

                st.write("Step 3: Creating vector store...")

                vectorstore = get_vectorstore(chunked_documents)

                st.write("Step 4: Building conversation chain...")

                st.session_state.conversation = get_conversation_chain(
                    vectorstore
                )

                st.success("Done!")

                st.success(f"✓ Processed {num_pdfs} PDF(s)")
                st.info(f"📄 Total pages: {num_pages}")
                st.info(f"🧩 Total chunks: {num_chunks}")
        st.markdown("---")

        if st.session_state.document_info:
           st.success("🟢 Ready to Chat")
        else:
           st.warning("🔴 No documents processed")

        if st.session_state.document_info:

           st.subheader("Processed Documents")

           for doc in st.session_state.document_info:

            st.success(f"✓ {doc['name']}")
            st.caption(f"📄 {doc['pages']} page(s)")
                
        if st.button("🗑 Clear Documents"):

            st.session_state.document_info = []
            st.session_state.conversation = None
            st.session_state.chat_history = None

           # Clear all document checkbox states
            for key in list(st.session_state.keys()):
              if key.startswith("doc_"):
                del st.session_state[key]

            st.experimental_rerun()

if __name__ == "__main__":
    main()
