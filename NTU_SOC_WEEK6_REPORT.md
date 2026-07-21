# NTU Summer of Code 2026
## Week 6 Progress Report

### Objective

This week's goal was to improve the overall usability of the application by giving users more control over document processing and introducing better document management features. The focus was on creating a smoother workflow rather than changing the retrieval pipeline itself.

---

## Features Implemented

### 1. Document Selection

Implemented individual checkboxes for every uploaded PDF, allowing users to choose which documents should be processed instead of automatically processing every uploaded file.

---

### 2. Select All / Deselect All

Added quick selection buttons that allow users to select or deselect all uploaded documents with a single click. Document selection states are preserved using Streamlit's session state.

---

### 3. Selective Processing Pipeline

Updated the processing workflow so that only the selected PDFs are:

- Read
- Split into chunks
- Embedded
- Indexed using FAISS

This reduces unnecessary processing and provides greater flexibility when working with multiple documents.

---

### 4. Input Validation

Added validation before processing begins.

If no document has been selected, the application now displays an informative warning instead of attempting to process an empty document list.

---

### 5. Processed Documents Panel

Introduced a new sidebar section that displays all processed documents after indexing.

Each processed document remains visible throughout the session using Streamlit session state.

---

### 6. Page Count Display

Added page count information for every processed PDF, allowing users to quickly verify the uploaded documents.

Example:

✓ Resume.pdf

📄 2 pages

---

### 7. Application Status Indicator

Implemented a visual status indicator showing the current state of the application.

States include:

🟢 Ready to Chat

🔴 No Documents Processed

This provides immediate feedback about whether the chatbot is ready for querying.

---

### 8. Clear Documents

Implemented a reset feature that clears:

- processed document information
- conversation chain
- chat history
- selected documents

This allows users to start a completely fresh session without refreshing the application.

---

### 9. Improved Error Handling

Fixed an issue where asking a question after clearing documents caused the application to crash because no conversation chain existed.

The application now detects this situation and prompts the user to process documents first instead of raising an exception.

---

## Challenges

The biggest challenge this week was managing Streamlit's session state while keeping the interface synchronized across reruns.

Additional effort was required to maintain compatibility with the project's existing dependency versions, particularly the older Streamlit release.

---

## Skills Applied

- Python
- Streamlit
- Session State Management
- User Interface Design
- FAISS Workflow
- Debugging
- Application State Management

---

## Outcome

Week 6 significantly improved the user experience of the application by making document processing more flexible and transparent. Users now have complete control over which documents are processed, can easily manage processed files, and receive clear visual feedback about the application's current state.

These improvements establish a solid foundation for Week 7, which will focus on preserving document metadata and improving source attribution.