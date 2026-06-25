# Week 2 Feature Investigation

## Selected Feature

Display Source PDF Name and Page Number for Every Answer

## Current Architecture

PDF Upload
→ Text Extraction (PyPDF2)
→ Text Chunking
→ OpenAI Embeddings
→ FAISS Vector Store
→ Conversational Retrieval Chain
→ Generated Answer

## Problem

The application currently provides answers without showing which PDF or page the information came from.

Users cannot verify the accuracy of generated responses or trace information back to the original source.

## Investigation Findings

### get_pdf_text()

The function extracts text from every page and combines it into a single string.

Result:

* PDF filename information is lost
* Page number information is lost

### get_text_chunks()

The function splits the combined text into chunks.

Result:

* Chunks contain text only
* No metadata is preserved

### get_vectorstore()

The application uses:

FAISS.from_texts()

Result:

* Only text embeddings are stored
* Source metadata is not stored

### handle_userinput()

The application only displays chat history.

Result:

* Source documents are not shown to the user

## Root Cause

Metadata is discarded before chunking and vector storage.

Because the vector store only contains text, retrieved chunks cannot be traced back to their original PDF and page.

## Proposed Solution

1. Preserve PDF filename metadata.
2. Preserve page number metadata.
3. Store chunks as LangChain Documents.
4. Replace FAISS.from_texts() with FAISS.from_documents().
5. Enable source document retrieval.
6. Display source PDF names and page numbers with answers.

## Expected Outcome

Users will be able to see which PDF and page were used to generate each answer, improving transparency and trust.

