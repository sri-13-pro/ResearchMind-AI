"""
===========================================================
ResearchMind AI
Intelligent Research Paper Analysis System
===========================================================
"""

import os
import sys
import pandas as pd

from utils.banner import show_banner
from utils.pdf_utils import extract_text_from_pdf
from utils.preprocessing import preprocess
from utils.summarizer import PaperSummarizer
from utils.analytics import PaperAnalytics
from utils.citation import CitationGenerator
from utils.report_generator import generate_report
from utils.semantic_search import SemanticSearch

# ===========================================================
# Banner
# ===========================================================

def banner():

    os.system("cls" if os.name == "nt" else "clear")

    show_banner()


# ===========================================================
# Pause
# ===========================================================

def pause():

    input("\nPress ENTER to continue...")


# ===========================================================
# About
# ===========================================================

def about():

    banner()

    print("""
ResearchMind AI

Version : 2.0

Developed Using

• Python

• Natural Language Processing

• Sentence Transformers

• FAISS

• WordCloud

• ReportLab

• Matplotlib

• Hugging Face

• Jupyter Notebook

ResearchMind AI helps researchers analyze research papers,
generate summaries, keywords, statistics, semantic search
and professional reports.
""")

    pause()


# ===========================================================
# Select PDF
# ===========================================================

def select_pdf():

    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    pdfs = [
        f for f in os.listdir("uploads")
        if f.lower().endswith(".pdf")
    ]

    if len(pdfs) == 0:

        banner()

        print("No PDF files found inside uploads folder.")

        pause()

        return None

    while True:

        banner()

        print("Available Research Papers\n")

        for i, pdf in enumerate(pdfs, start=1):

            print(f"{i}. {pdf}")

        print()

        choice = input("Choose PDF : ")

        try:

            choice = int(choice)

            if 1 <= choice <= len(pdfs):

                return os.path.join(
                    "uploads",
                    pdfs[choice - 1]
                )

        except:
            pass

        print("\nInvalid Choice!")

        pause()


# ===========================================================
# Analyze Research Paper
# ===========================================================

def analyze():

    pdf = select_pdf()

    if pdf is None:
        return

    banner()

    print("Loading Research Paper...\n")

    text = extract_text_from_pdf(pdf)

    print("✔ PDF Loaded")

    print(f"\nCharacters : {len(text)}")

    print("\nGenerating Summary...")

    summarizer = PaperSummarizer()

    summary = summarizer.summarize(
        text,
        sentences=5
    )

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    for sentence in summary:

        print("•", sentence)

    print("\nGenerating Keywords...")

    keywords = summarizer.keywords(
        text,
        top_n=10
    )

    print()

    for keyword, score in keywords:

        print(f"• {keyword}")

    analytics = PaperAnalytics(text)

    print("\n" + "=" * 70)
    print("STATISTICS")
    print("=" * 70)

    stats = analytics.statistics()

    for key, value in stats.items():

        print(f"{key:35}: {value}")

    print("\nGenerating Word Cloud...")

    analytics.word_cloud()

    print("✔ Word Cloud Saved")

    print("\nGenerating Frequency Chart...")

    analytics.plot_frequency()

    print("✔ Frequency Chart Saved")

    print("\nGenerating PDF Report...")

    report = generate_report(

        title=os.path.basename(pdf),

        summary=summary,

        keywords=keywords,

        statistics=stats

    )

    print(f"\n✔ Report Saved : {report}")

    print("\nAnalysis Completed Successfully!")

    pause()
# ===========================================================
# Semantic Search
# ===========================================================

def semantic_search():

    banner()

    csv_path = "data/cleaned_papers.csv"

    if not os.path.exists(csv_path):

        print("Dataset not found!")

        pause()

        return

    print("Loading dataset...")

    papers = pd.read_csv(csv_path)

    engine = SemanticSearch()

    if engine.load():

        print("✔ Existing vector index loaded.")

    else:

        print("Creating vector database...")

        embeddings = engine.create_embeddings(papers)

        engine.build_index(embeddings)

        engine.save()

        print("✔ Vector database created.")

    while True:

        print()

        query = input(
            "Enter search query (or type 'back'): "
        )

        if query.lower() == "back":
            return

        print("\nSearching...\n")

        results = engine.search(query, top_k=5)

        print("=" * 70)
        print("Top Matching Research Papers")
        print("=" * 70)

        for i, idx in enumerate(results, start=1):

            row = papers.iloc[idx]

            print(f"\n{i}. {row['title']}")

            print("-" * 70)

            abstract = str(row["abstract"])

            print(abstract[:350] + "...")

            print()


# ===========================================================
# Citation Generator
# ===========================================================

def citation():

    pdf = select_pdf()

    if pdf is None:
        return

    title = os.path.basename(pdf).replace(".pdf", "")

    cite = CitationGenerator(

        title=title,

        authors="Unknown Author",

        year="2025"

    )

    banner()

    print("=" * 70)
    print("APA")
    print("=" * 70)

    print(cite.apa())

    print("\n" + "=" * 70)
    print("IEEE")
    print("=" * 70)

    print(cite.ieee())

    print("\n" + "=" * 70)
    print("MLA")
    print("=" * 70)

    print(cite.mla())

    pause()


# ===========================================================
# Main Menu
# ===========================================================

def menu():

    while True:

        banner()

        print("1. Analyze Research Paper")
        print("2. Semantic Search")
        print("3. Generate Citation")
        print("4. About")
        print("5. Exit")

        print()

        choice = input("Enter Choice : ")

        if choice == "1":

            analyze()

        elif choice == "2":

            semantic_search()

        elif choice == "3":

            citation()

        elif choice == "4":

            about()

        elif choice == "5":

            banner()

            print("Thank you for using ResearchMind AI!")

            sys.exit()

        else:

            print("\nInvalid Choice!")

            pause()


# ===========================================================
# Main
# ===========================================================

if __name__ == "__main__":

    menu()
