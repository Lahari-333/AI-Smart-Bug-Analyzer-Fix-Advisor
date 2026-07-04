# AI Smart Bug Analyzer & Fix Advisor

## Overview

AI Smart Bug Analyzer & Fix Advisor is an AI-powered system developed as part of the Infosys Springboard Internship. The project helps developers analyze software bug reports, retrieve similar historical defects using Retrieval-Augmented Generation (RAG), and provide possible fix suggestions and severity prediction.

---

## Milestone 1 Objectives

- Study defect analysis workflows
- Understand RAG architecture
- Learn semantic similarity techniques
- Analyze bug report structures
- Design system architecture
- Develop the Bug Submission Module
- Build the initial Historical Defect Knowledge Base

---

## Features Implemented

- Bug report submission
- Direct text input for bug reports
- Stack trace and error log input
- File upload support
- Dataset exploration and analysis
- Initial project architecture

---

## Tech Stack

- Python
- Streamlit
- NumPy
- Pandas
- RAG (Retrieval-Augmented Generation)
- Semantic Similarity
- Bugzilla Dataset

---

## Project Structure

```
AI-Smart-Bug-Analyzer/
│
├── app.py
├── README.md
├── .gitignore
├── documentation/
└── screenshots/
```

---

## Dataset

This project uses public Bugzilla historical bug datasets (Mozilla, Apache, and Eclipse repositories).

Due to GitHub's file size limitations, the dataset is not included in this repository.

The dataset used during development includes:

- corpus (fixsev).txt
- embedding.npy
- fix.csv
- fix_train.csv
- fix_test.csv
- sev.csv
- sev_train.csv
- sev_test.csv
- vocab.lst

---

## Future Enhancements

- Historical Defect Knowledge Base
- Embedding Generation
- Vector Database (FAISS)
- Duplicate Bug Detection
- Root Cause Analysis
- AI-based Fix Recommendation
- Severity Prediction

---

## Internship

Project developed as part of the **Infosys Springboard Internship Program**.
