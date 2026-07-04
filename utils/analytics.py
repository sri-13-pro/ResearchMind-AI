"""
===========================================================
Paper Analytics
ResearchMind AI
===========================================================
"""

import os
import re

import matplotlib.pyplot as plt
import pandas as pd

from collections import Counter
from wordcloud import WordCloud


class PaperAnalytics:

    def __init__(self, text):

        self.text = text

    # -----------------------------------------------------

    def words(self):

        return re.findall(
            r"\b[a-zA-Z]{3,}\b",
            self.text.lower()
        )

    # -----------------------------------------------------

    def statistics(self):

        words = self.words()

        return {

            "Characters": len(self.text),

            "Words": len(words),

            "Unique Words": len(set(words)),

            "Estimated Reading Time (minutes)": round(
                len(words) / 200,
                2
            )

        }

    # -----------------------------------------------------

    def frequent_words(self, top_n=20):

        counter = Counter(self.words())

        df = pd.DataFrame(

            counter.most_common(top_n),

            columns=["Word", "Frequency"]

        )

        return df

    # -----------------------------------------------------

    def plot_frequency(self, top_n=20):

        os.makedirs("reports", exist_ok=True)

        df = self.frequent_words(top_n)

        plt.figure(figsize=(12,6))

        plt.bar(

            df["Word"],

            df["Frequency"]

        )

        plt.title("Top Frequent Words")

        plt.xlabel("Words")

        plt.ylabel("Frequency")

        plt.xticks(rotation=45)

        plt.tight_layout()

        save_path = os.path.join(

            "reports",

            "frequency_chart.png"

        )

        plt.savefig(

            save_path,

            dpi=300

        )

        plt.close()

        print(f"Frequency Chart Saved → {save_path}")

    # -----------------------------------------------------

    def word_cloud(self):

        os.makedirs("reports", exist_ok=True)

        wc = WordCloud(

            width=1600,

            height=800,

            background_color="white",

            colormap="viridis"

        ).generate(self.text)

        plt.figure(figsize=(15,8))

        plt.imshow(wc)

        plt.axis("off")

        plt.tight_layout()

        save_path = os.path.join(

            "reports",

            "wordcloud.png"

        )

        plt.savefig(

            save_path,

            dpi=300,

            bbox_inches="tight"

        )

        plt.close()

        print(f"Word Cloud Saved → {save_path}")

    # -----------------------------------------------------

    def export_statistics(self):

        os.makedirs("reports", exist_ok=True)

        stats = self.statistics()

        df = pd.DataFrame(

            stats.items(),

            columns=["Metric","Value"]

        )

        save_path = os.path.join(

            "reports",

            "statistics.csv"

        )

        df.to_csv(

            save_path,

            index=False

        )

        print(f"Statistics Saved → {save_path}")

    # -----------------------------------------------------

    def export_keywords(self, keywords):

        os.makedirs("reports", exist_ok=True)

        df = pd.DataFrame(

            keywords,

            columns=["Keyword","Score"]

        )

        save_path = os.path.join(

            "reports",

            "keywords.csv"

        )

        df.to_csv(

            save_path,

            index=False

        )

        print(f"Keywords Saved → {save_path}")