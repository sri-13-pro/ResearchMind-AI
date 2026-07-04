"""
===========================================================
PDF Utility Functions
AI Research Paper Intelligence System
===========================================================

This module contains functions to:
1. Open a PDF
2. Extract text
3. Clean extracted text
4. Save extracted text
"""

import fitz
import os


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.

    Parameters
    ----------
    pdf_path : str
        Path to the PDF

    Returns
    -------
    str
        Extracted text
    """

    try:
        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    except Exception as e:
        print("Error:", e)
        return ""


def clean_text(text):
    """
    Remove unnecessary spaces and line breaks.
    """

    text = " ".join(text.split())

    return text


def save_text(text, output_path):
    """
    Save extracted text into a text file.
    """

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)

    print("✅ Text saved successfully!")


def get_pdf_info(pdf_path):
    """
    Return PDF information.
    """

    document = fitz.open(pdf_path)

    info = {
        "Pages": len(document),
        "Title": document.metadata.get("title"),
        "Author": document.metadata.get("author")
    }

    document.close()

    return info