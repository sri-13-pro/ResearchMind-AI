"""
===========================================================
Citation Utilities
AI Research Paper Intelligence System
===========================================================
"""

class CitationGenerator:

    def __init__(self, title, authors="Unknown Author", year="2025"):
        self.title = title
        self.authors = authors
        self.year = year

    def apa(self):
        return f"{self.authors} ({self.year}). {self.title}."

    def ieee(self):
        return f"{self.authors}, \"{self.title},\" {self.year}."

    def mla(self):
        return f"{self.authors}. \"{self.title}.\" {self.year}."