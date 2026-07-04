# ⚙️ Utils

This folder contains the core modules that power **ResearchMind AI**.

Each module is responsible for a specific part of the application.

---

## Modules

### analytics.py

Provides research paper analytics including:

- Text statistics
- Word frequency
- Word cloud generation
- Frequency chart generation

---

### banner.py

Displays the application banner and branding.

---

### citation.py

Generates citations in multiple formats:

- APA
- IEEE
- MLA

---

### loading.py

Displays loading animations and progress indicators.

---

### pdf_utils.py

Extracts text from PDF research papers using PyMuPDF.

---

### preprocessing.py

Implements text preprocessing including:

- Cleaning
- Tokenization
- Stopword removal
- Lemmatization

---

### report_generator.py

Generates professional PDF reports using ReportLab.

---

### semantic_search.py

Implements semantic search using:

- Sentence Transformers
- FAISS Vector Database

---

### summarizer.py

Performs:

- Research paper summarization
- Keyword extraction

---

## Design

The project follows a modular architecture where each module is responsible for a single task, improving maintainability, readability, and scalability.
