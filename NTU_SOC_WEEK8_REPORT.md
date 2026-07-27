# NTU Summer of Code 2026 — Week 8 Report

## Project

**Ask Multiple PDFs — Retrieval-Augmented Generation (RAG) Application**

## Week 8 Focus

**Final Application Hardening, Error Handling, Accuracy Improvements, Testing, and Project Completion**

---

## 1. Overview

Week 8 focused on preparing the Ask Multiple PDFs application for final completion. Rather than introducing unnecessary new functionality, the focus was on improving reliability, handling edge cases, correcting inaccurate processing statistics, removing temporary development code, and conducting comprehensive end-to-end testing.

The goal was to ensure that the application was stable, user-friendly, and suitable for final submission and continued use.

---

## 2. Improvements Implemented

### 2.1 Graceful PDF Processing Error Handling

The PDF processing workflow was improved to handle invalid, corrupted, or unreadable PDF files without crashing the application.

Previously, an unreadable PDF could cause an exception and interrupt the entire processing workflow.

A `try/except` mechanism was added around PDF reading so that users receive a clear warning when a PDF cannot be processed.

Example user-facing message:

> ⚠️ Could not process 'test_invalid.pdf'. Please make sure it is a valid, readable PDF.

This makes the application more robust and prevents raw Python errors from being exposed to users.

---

### 2.2 Handling PDFs With No Extractable Text

An additional validation step was introduced to detect situations where no readable text can be extracted from the selected PDFs.

If no readable documents are produced, the application now stops processing and provides a clear explanation:

> No readable text was found in the selected PDF(s). Please upload PDFs containing extractable text.

This prevents the application from continuing into embedding and retrieval steps with an empty document collection.

---

### 2.3 Accurate PDF Page Count Reporting

The application previously calculated the total number of pages using the number of successfully extracted document objects.

This could produce an inaccurate count when some PDF pages contained no extractable text.

The page-count calculation was improved to use the actual number of pages in each uploaded PDF.

The application now correctly distinguishes between:

* Physical PDF pages
* Extracted text chunks

For example, during final testing:

* `DevanshPoddarResume.pdf` — 2 pages
* `CC0001 Assignment 3 - Devansh Poddar.pdf` — 4 pages
* **Total pages — 6**
* **Total chunks — 9**

This provides more accurate processing statistics to the user.

---

### 2.4 Code Cleanup

Temporary development and debugging code was removed before finalization.

This included:

* Debugging `print()` statements
* Source-document metadata dumps
* Document preview output used during development
* Unused Hugging Face imports
* Obsolete commented-out Hugging Face implementation code

The final application code is therefore cleaner and more focused on the actual implementation being used.

---

## 3. Final Application Features

By the end of Week 8, the application provides:

* Multiple PDF upload support
* Individual document selection
* Select All / Deselect All functionality
* PDF processing and text extraction
* Text chunking with overlap
* OpenAI embeddings
* FAISS vector storage
* Conversational retrieval using LangChain
* Chat history
* Multi-document question answering
* Source document attribution
* Page-level source attribution
* Grouped evidence display
* Highlighting of relevant answer words in evidence snippets
* Document processing statistics
* Processed-document information
* Ready-to-chat status
* Clear Documents functionality
* Safe handling of questions before documents are processed
* Graceful handling of invalid PDFs
* Graceful handling of PDFs with no extractable text
* Accurate physical page-count reporting

---

## 4. Testing and Validation

A comprehensive final test was conducted after the Week 8 changes.

### Functional testing

The following workflows were successfully tested:

* Uploading multiple PDFs
* Selecting individual documents
* Selecting all documents
* Deselecting all documents
* Processing selected documents
* Generating embeddings
* Building the FAISS vector store
* Building the conversation chain
* Asking questions about processed documents
* Displaying answers and chat history
* Displaying source filenames
* Displaying source page numbers
* Displaying grouped evidence
* Clearing processed documents
* Reprocessing documents after clearing

### Edge-case testing

The following cases were also tested successfully:

* Asking a question before processing any document
* Attempting to process without selecting a document
* Uploading an invalid PDF
* Uploading a PDF with no extractable text
* Processing multiple documents simultaneously

The invalid PDF test successfully produced a user-friendly warning without crashing the application.

### Code validation

The final `app.py` successfully passed Python compilation checks using:

```bash
python -m py_compile app.py
```

The Streamlit application also launched successfully after the final changes.

---

## 5. Git and Version Control

All Week 8 development work was completed on the dedicated `feature/week8` branch.

The major Week 8 commits included:

```text
feat: add graceful PDF processing error handling
fix: report accurate PDF page counts
```

The Week 8 branch was successfully pushed to the remote GitHub repository.

The project now contains a structured development history across the eight-week NTU Summer of Code period.

---

## 6. Overall Project Progress

Across the eight weeks, the project evolved from a basic PDF question-answering implementation into a more complete multi-document RAG application.

Major areas of development included:

1. Initial RAG application setup
2. PDF ingestion and text processing
3. Vector search and conversational retrieval
4. Evidence and source citation improvements
5. Multi-document selection and processing
6. Document management and application workflow
7. Metadata preservation and source attribution
8. Final reliability, error handling, accuracy improvements, cleanup, and testing

The final application provides a substantially improved user experience compared with the initial implementation.

---

## 7. Reflection

The final week highlighted the importance of software engineering practices beyond simply adding new features.

Testing edge cases revealed areas where the application could fail or provide misleading information. Handling invalid PDFs, validating extracted content, and correcting page-count calculations improved the reliability and trustworthiness of the system.

The cleanup process also reinforced the importance of removing temporary debugging code and unused dependencies before finalizing a project.

Overall, the project provided practical experience with:

* Retrieval-Augmented Generation
* Large Language Models
* Embeddings
* Vector databases
* FAISS
* LangChain
* Streamlit
* PDF processing
* Metadata preservation
* Source attribution
* Error handling
* State management
* Git and GitHub workflows
* Testing and debugging
* Iterative software development

---

## 8. Conclusion

Week 8 successfully completed the development phase of the Ask Multiple PDFs project.

The final application is stable, tested, and capable of handling multiple documents while providing source-aware answers and evidence. The final improvements focused on reliability, accuracy, user experience, and maintainability rather than unnecessary feature expansion.

The project is now ready for final repository cleanup, merging the completed work into the main branch, and final submission.
