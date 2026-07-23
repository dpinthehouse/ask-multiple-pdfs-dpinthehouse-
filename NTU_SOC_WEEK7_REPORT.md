# NTU Summer of Code 2026 – Week 7 Report

## Name
Devansh Poddar

## Project
Ask Multiple PDFs

## Week
Week 7

---

## Objectives

This week's objective was to improve the reliability of document retrieval by preserving document metadata throughout the retrieval pipeline and displaying accurate source citations with every generated answer.

---

## Features Implemented

### 1. Metadata Preservation

- Updated the PDF processing pipeline to attach metadata to every page.
- Stored:
  - PDF filename
  - Page number
- Preserved metadata while splitting documents into chunks.

---

### 2. FAISS Metadata Storage

- Replaced manual embedding creation with `FAISS.from_documents()`.
- Ensured metadata is stored together with every document chunk.
- Fixed the issue where retrieved documents contained empty metadata.

---

### 3. Source Attribution

Added proper source attribution for every retrieved document.

Displayed:

- PDF filename
- Page number

instead of

- Unknown Source
- Unknown Page

---

### 4. Grouped Evidence Display

Grouped retrieved chunks by:

- Source document
- Page number

Displayed grouped supporting evidence inside expandable sections.

---

### 5. Evidence Ranking

Added ranked source labels:

- 🥇 Most Relevant
- 🥈 Relevant
- 🥉 Additional Context

to improve readability.

---

## Bug Fixes

Resolved an issue where retrieved documents returned empty metadata after vector store creation.

Root cause:

- Metadata was lost when manually creating embeddings using `FAISS.from_embeddings()`.

Solution:

- Switched to `FAISS.from_documents()` which preserves metadata automatically.

---

## Testing Performed

Verified:

- Single-document retrieval
- Multiple-document retrieval
- Correct filename display
- Correct page-number display
- Source grouping
- Source ranking

All tests passed successfully.

---

## Skills Learned

- LangChain Document metadata
- Metadata propagation through text splitting
- FAISS document storage
- Retrieval pipeline debugging
- Source attribution for Retrieval-Augmented Generation (RAG)

---

## Status

Week 7 completed successfully.

The application now provides transparent, verifiable answers by displaying the exact document and page used to generate each response.
