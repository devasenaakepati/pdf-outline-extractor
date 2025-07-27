# Adobe Hackathon 2025 - PDF Outline Extractor

## 🧠 Purpose
Extracts structured outlines from PDFs — including title and heading hierarchy (H1, H2, H3) with page numbers.

## 🚀 Run Instructions

### Build Docker Image

```bash
docker build --platform linux/amd64 -t pdf-outliner:extractor .

This project is a simple offline PDF Outline Extractor built using **Python** and **PyMuPDF**. It identifies and extracts the **document title**, and hierarchical **headings (H1, H2, H3)** based on font-size analysis.

---

## 📌 Features

- ✅ Runs fully offline — no API keys or internet required
- ✅ Extracts title and headings using font size heuristics
- ✅ Supports PDFs up to 50 pages
- ✅ Outputs structured JSON format
- ✅ Streamlit interface for file upload and preview

---

## 🛠️ Technologies Used

- Python 3.x
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- Streamlit


