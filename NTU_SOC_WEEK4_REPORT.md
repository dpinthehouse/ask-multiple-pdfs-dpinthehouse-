# NTU Summer of Code – Week 4 Progress Report

## Objective

The objective for Week 4 was to improve the transparency, usability, and overall user experience of the document question-answering system. The focus was on enhancing how retrieved evidence is presented while giving users more insight into how answers are generated.

---

## Work Completed

### 1. Preserved Source Metadata

- Maintained PDF filename and page number information during document processing.
- Ensured retrieved answers correctly referenced the original document source.

### 2. Improved Evidence Organization

- Grouped retrieved evidence by document and page number.
- Removed duplicate evidence snippets to reduce redundancy.

### 3. Evidence Highlighting

- Implemented keyword highlighting within retrieved evidence snippets.
- Improved readability by emphasizing important answer-related terms.

### 4. Cleaner Evidence Display

- Reduced evidence snippet length from approximately 300 characters to 180 characters.
- Added expandable evidence cards using Streamlit expanders for a cleaner interface.

### 5. Evidence Ranking

Added relevance labels for retrieved evidence:

- 🥇 Most Relevant
- 🥈 Relevant
- 🥉 Additional Context
- 📄 Supporting Evidence

### 6. Retrieval Statistics

- Displayed the number of document excerpts used to support each generated answer.

### 7. Processing Statistics

After document processing, the application now displays:

- Number of uploaded PDFs
- Total pages processed
- Total text chunks created

### 8. Response Time Monitoring

- Measured and displayed answer generation time for every user query.

---

## Challenges Faced

During development, several technical issues were encountered and resolved:

- Corrected Streamlit sidebar layout after UI modifications.
- Fixed indentation and formatting issues introduced during interface restructuring.
- Resolved `tiktoken` installation and network download issues.
- Verified metadata propagation throughout the retrieval pipeline.
- Ensured all new features integrated correctly without affecting existing functionality.

---

## Outcome

The application now provides a significantly more transparent and user-friendly retrieval experience. Users receive better-organized supporting evidence, relevance rankings, processing statistics, and response timing, making the retrieval process easier to understand and increasing confidence in the generated answers.