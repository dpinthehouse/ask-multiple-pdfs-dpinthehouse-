# NTU SoC - Week 3 Progress Report

## Feature
Evidence-Based Source Citations

## Objective
Improve the transparency of chatbot responses by displaying supporting evidence retrieved from the uploaded PDF documents.

## Changes Implemented
- Added evidence snippets by displaying the first 300 characters of each retrieved document chunk.
- Displayed the PDF filename and page number alongside every evidence snippet.
- Grouped evidence by PDF and page to avoid repeating the same source heading multiple times.
- Filtered duplicate snippets within each grouped source.
- Tested the feature with multiple questions spanning different PDF documents.

## Example

### Before
```
Sources

• DevanshPoddarResume-2.pdf (Page 1)
```

### After
```
Sources

📄 DevanshPoddarResume-2.pdf (Page 1)

Devansh Poddar
Education
Nanyang Technological University Singapore...

AI Scholar
Completed a 10-week intensive program...

------------------------------------------------

📄 CC0001 Assignment 3 - Devansh Poddar.pdf (Page 1)

Declaration of Academic Integrity...
```

## Outcome
Users can now inspect supporting evidence retrieved from the source documents instead of only viewing the document name and page number. This improves transparency and helps users understand why the chatbot generated a particular answer.