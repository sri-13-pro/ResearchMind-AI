"""
===========================================================
ResearchMind AI
Intelligent Research Paper Analysis System
===========================================================
"""

import os
import sys
from utils.banner import show_banner

show_banner()
import pandas as pd
from utils.semantic_search import SemanticSearch
from utils.pdf_utils import extract_text_from_pdf
from utils.preprocessing import preprocess
from utils.summarizer import PaperSummarizer
from utils.analytics import PaperAnalytics
from utils.citation import CitationGenerator
from utils.report_generator import generate_report


# ===========================================================
# Banner
# ===========================================================

def banner():

    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 70)
    print("                🤖 ResearchMind AI")
    print("     Intelligent Research Paper Analysis System")
    print("=" * 70)


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

Version : 1.0

Developed Using

• Python

• NLP

• Sentence Transformers

• FAISS

• WordCloud

• ReportLab

• Matplotlib

• Jupyter Notebook

Created as an AI Portfolio Project.
""")

    pause()


# ===========================================================
# Select PDF
# ===========================================================

def select_pdf():

    while True:

        banner()

        print("Available PDFs:\n")

        if not os.path.exists("uploads"):
            os.makedirs("uploads")

        pdfs = [
            file
            for file in os.listdir("uploads")
            if file.lower().endswith(".pdf")
        ]

        if len(pdfs) == 0:

            print("No PDF found inside uploads folder.")

            pause()

            return None

        for i, pdf in enumerate(pdfs, start=1):

            print(f"{i}. {pdf}")

        print()

        choice = input("Enter PDF number: ")

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
# Analyze Paper
# ===========================================================

def analyze():

    pdf = select_pdf()

    if pdf is None:
        return

    banner()

    print("Loading PDF...")

    text = extract_text_from_pdf(pdf)

    print("✔ PDF Loaded")

    print("\nCharacters :", len(text))

    print("\nGenerating Summary...")

    summarizer = PaperSummarizer()

    summary = summarizer.summarize(
        text,
        sentences=5
    )

    print("\nSUMMARY")
    print("-" * 60)

    for sentence in summary:
        print("•", sentence)

    print("\nExtracting Keywords...")

    keywords = summarizer.keywords(
        text,
        top_n=10
    )

    print()

    for keyword, score in keywords:
        print("•", keyword)

    print("\nCalculating Statistics...")

    analytics = PaperAnalytics(text)

    print()

    for key, value in analytics.statistics().items():

        print(f"{key:35} : {value}")

    print("\nGenerating Charts...")

    analytics.word_cloud()

    analytics.plot_frequency()
    print("\nGenerating PDF Report...")

    report = generate_report(
         title=os.path.basename(pdf),
         summary=summary,
         keywords=keywords,
         statistics=analytics.statistics()
)

    print(f"✔ Report saved to: {report}")

    print("\nAnalysis Completed Successfully!")

    pause()


# ===========================================================
# Citation
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

    print("APA\n")

    print(cite.apa())

    print("\nIEEE\n")

    print(cite.ieee())

    print("\nMLA\n")

    print(cite.mla())

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

    search_engine = SemanticSearch()

    if not search_engine.load():

        print("Building vector database...")

        embeddings = search_engine.create_embeddings(papers)

        search_engine.build_index(embeddings)

        search_engine.save()

    print()

    query = input("Enter your search query: ")

    print("\nSearching...\n")

    results = search_engine.search(query, top_k=5)

    print("=" * 70)

    print("Top Matching Papers")

    print("=" * 70)

    for i, idx in enumerate(results, start=1):

        row = papers.iloc[idx]

        print(f"\n{i}. {row['title']}")

        print("-" * 70)

        print(row["abstract"][:300] + "...")

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

if __name__ == "__main__":

    menu()