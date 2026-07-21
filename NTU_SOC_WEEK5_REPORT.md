# NTU Summer of Code 2026
## Week 5 Progress Report

### Objective
Improve the usability of the Ask Multiple PDFs application by allowing users to control which uploaded documents are included in the knowledge base before processing.

---

## Features Implemented

### 1. Document Selection
- Added checkboxes for every uploaded PDF.
- Users can choose which documents will be processed.

### 2. Select All / Deselect All
- Added buttons to quickly select or deselect every uploaded document.

### 3. Selection Counter
- Added a live counter displaying the number of selected documents.

Example:

Selected 2 of 3 document(s)

### 4. Processing Validation
- Added validation to prevent processing when no documents are selected.
- Displays a warning instead of continuing.

### 5. Improved Processing Workflow
Added progress updates showing:

- Reading PDFs
- Splitting text
- Creating vector store
- Building conversation chain

### 6. Processing Summary
After processing, the application now displays:

- Number of processed PDFs
- Total pages
- Total text chunks

---

## Testing

Verified the following scenarios:

- Process button disabled before uploading PDFs.
- Uploading PDFs enables processing.
- Select All works correctly.
- Deselect All works correctly.
- Processing only selected documents.
- Validation when no documents are selected.
- Successful vector store creation.
- Successful conversation chain creation.

---

## Outcome

The application now provides a significantly improved user experience by allowing users to control exactly which uploaded PDFs participate in document retrieval while providing better feedback throughout the processing pipeline.

---

## Skills Learned

- Streamlit session state management
- Dynamic checkbox generation
- Sidebar UI design
- User interaction validation
- Improving application usability