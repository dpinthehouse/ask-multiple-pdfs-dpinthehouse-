# Ask Multiple PDFs

A Retrieval-Augmented Generation (RAG) application that allows users to upload multiple PDF documents, select which documents to search, ask questions in natural language, and receive answers grounded in the uploaded documents.

The project was developed and substantially extended as part of **NTU Summer of Code 2026**, with a focus on improving document management, source attribution, evidence presentation, processing robustness, and overall application usability.

## Overview

Ask Multiple PDFs combines document processing, vector search, and large language models to provide a conversational interface for querying multiple PDF documents.

Users can:

* Upload multiple PDFs
* Select specific documents to include in a search
* Process selected documents into searchable text chunks
* Ask natural-language questions about their documents
* Receive answers generated from relevant document excerpts
* View the documents and pages supporting each answer
* See highlighted evidence relevant to the generated response
* Monitor document processing statistics
* Handle invalid or unreadable PDFs gracefully
* Clear processed documents and start a new session

## Key Features

### Multi-Document Selection

Users can upload multiple PDFs and choose exactly which documents should be included in the search.

The interface provides:

* **Select All**
* **Deselect All**
* Individual document selection
* A live count of selected documents

This allows users to work with only the documents relevant to their current question.

### RAG-Based Question Answering

The application uses a Retrieval-Augmented Generation pipeline:

1. PDF text is extracted using PyPDF2.
2. Extracted text is split into overlapping chunks.
3. OpenAI embeddings are generated for the chunks.
4. FAISS stores the resulting vectors.
5. Relevant chunks are retrieved for each question.
6. ChatOpenAI generates an answer using the retrieved context.

This allows users to ask questions about their documents using natural language.

### Source Attribution

Each extracted PDF page is stored with metadata containing:

* Source filename
* Page number

This metadata is preserved throughout the document chunking and retrieval pipeline.

As a result, answers can be accompanied by page-level source information rather than displaying only the generated response.

### Evidence Presentation

The application displays supporting evidence below each answer.

Sources are grouped by:

* Document
* Page

The interface also provides relevance labels such as:

* 🥇 Most Relevant
* 🥈 Relevant
* 🥉 Additional Context
* 📄 Supporting Evidence

Relevant words from the generated answer are highlighted within source snippets to make verification easier.

### Processing Feedback

During document processing, the application provides feedback for each stage:

1. Reading PDFs
2. Splitting text
3. Creating vector store
4. Building conversation chain

It also reports:

* Number of processed PDFs
* Total number of pages
* Number of generated chunks
* Embedding progress

### Document Management

The sidebar provides a summary of the current document-processing state.

For each processed document, the application displays:

* Filename
* Number of pages

The interface also indicates whether the application is:

* 🟢 Ready to Chat
* 🔴 No documents processed

A **Clear Documents** control allows users to reset the current document-processing session.

### Error Handling

The application handles PDF processing failures without crashing the Streamlit application.

Invalid or unreadable PDFs are reported to the user with a clear warning.

The application also checks whether any readable text was extracted and prevents the user from continuing when no extractable text is available.

This prevents downstream failures during chunking, embedding generation, and conversation-chain creation.

### Response Information

After each question, the interface displays:

* Generated answer
* Response generation time
* Number of supporting document excerpts
* Supporting source documents and pages

This provides users with additional information about how the answer was produced.

## Architecture

```text
PDF Upload
    ↓
Document Selection
    ↓
PDF Text Extraction
    ↓
Page Metadata Preservation
    ↓
Text Chunking
    ↓
OpenAI Embeddings
    ↓
FAISS Vector Store
    ↓
Similarity Retrieval
    ↓
Conversational Retrieval Chain
    ↓
ChatOpenAI
    ↓
Generated Answer
    ↓
Source Attribution + Evidence
```

## Tech Stack

* **Python**
* **Streamlit** — web application interface
* **LangChain** — RAG orchestration
* **PyPDF2** — PDF text extraction
* **OpenAI Embeddings** — document embeddings
* **FAISS** — vector similarity search
* **ChatOpenAI** — answer generation
* **python-dotenv** — environment variable management

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/dpinthehouse/ask-multiple-pdfs-dpinthehouse-.git
cd ask-multiple-pdfs-dpinthehouse-
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the OpenAI API key

Create a `.env` file in the project directory:

```env
OPENAI_API_KEY=your_openai_api_key
```

Do not commit your `.env` file or expose your API key publicly.

### 5. Run the application

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

## Usage

1. Upload one or more PDF documents.
2. Select the documents you want to search.
3. Click **Process**.
4. Wait for document processing and embedding generation to complete.
5. Enter a question about the selected documents.
6. Review the generated answer.
7. Expand the **Sources** section to inspect the supporting document excerpts and page numbers.
8. Use **Clear Documents** when you want to reset the current session.

## NTU Summer of Code 2026

This project was developed and improved over an **8-week NTU Summer of Code 2026** contribution period.

### Weekly Progress

| Week   | Focus                                                                                             |
| ------ | ------------------------------------------------------------------------------------------------- |
| Week 1 | Project understanding, existing architecture, and initial investigation                           |
| Week 2 | Investigation and design of source citation capabilities                                          |
| Week 3 | Initial implementation and project improvements                                                   |
| Week 4 | Evidence and source-related feature development                                                   |
| Week 5 | Multi-document selection and processing improvements                                              |
| Week 6 | Document management and application workflow improvements                                         |
| Week 7 | Source attribution and metadata preservation                                                      |
| Week 8 | Graceful PDF processing error handling, accurate page reporting, testing, and final documentation |

Detailed weekly reports are available in the repository:

* `NTU_SOC_WEEK2_REPORT.md`
* `NTU_SOC_WEEK3_REPORT.md`
* `NTU_SOC_WEEK4_REPORT.md`
* `NTU_SOC_WEEK5_REPORT.md`
* `NTU_SOC_WEEK6_REPORT.md`
* `NTU_SOC_WEEK7_REPORT.md`
* `NTU_SOC_WEEK8_REPORT.md`

## Testing

The application was manually tested throughout development, including:

* Multiple PDF uploads
* Individual document selection
* Select All / Deselect All
* Successful PDF processing
* Multi-document question answering
* Source filename attribution
* Page-level source attribution
* Evidence snippet display
* Evidence highlighting
* Document clearing
* Empty document selection
* Invalid PDF handling
* PDFs with no extractable text
* Accurate page-count reporting
* Application launch and end-to-end workflow

The final Week 8 workflow was verified successfully before merging the final version into `main`.

## Limitations

* PDF text extraction depends on PyPDF2's ability to extract readable text.
* Scanned/image-only PDFs may not produce usable text without OCR.
* Answer quality depends on the retrieved document context and the underlying language model.
* OpenAI API access is required for embeddings and answer generation.
* The application currently uses an in-memory session workflow rather than persistent document storage.

## Future Improvements

Potential future enhancements include:

* OCR support for scanned PDFs
* More advanced source-ranking methods
* Persistent vector stores
* Improved citation formatting
* Better conversation/session management
* Automated testing and CI/CD
* Support for additional document formats
* More advanced document-level filtering

## Acknowledgements

The initial application was based on the MultiPDF Chat App tutorial by tgifhacks. The project was subsequently extended and improved as part of NTU Summer of Code 2026.

## License

This project is released under the MIT License.
