# Feature Design: Source PDF and Page Number Citations

## Goal

Display the source PDF filename and page number used to generate each answer.

## Current Workflow

PDF Upload
→ Text Extraction
→ Text Chunking
→ Embeddings
→ FAISS.from_texts()
→ Conversational Retrieval Chain
→ Answer

## Problem

Metadata is lost during text extraction and chunking.

As a result:

* PDF filename is unavailable
* Page number is unavailable
* Users cannot verify answers

## Proposed Workflow

PDF Upload
→ Create Documents with Metadata
→ Chunk Documents
→ FAISS.from_documents()
→ Conversational Retrieval Chain
→ Answer + Source Documents
→ Display Citations

## Metadata Structure

source: PDF filename

page: Page number

## Implementation Steps

1. Modify PDF extraction to preserve metadata.
2. Create LangChain Document objects.
3. Chunk Document objects instead of raw text.
4. Replace FAISS.from_texts() with FAISS.from_documents().
5. Enable source document retrieval.
6. Display source citations in the UI.

## Expected Result

Example:

Answer:
The company's revenue was $5 million.

Sources:
annual_report.pdf — Page 12
financial_report.pdf — Page 3
