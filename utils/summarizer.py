"""
===========================================================
Summarization Utilities
AI Research Paper Intelligence System
===========================================================
"""

import yake

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


class PaperSummarizer:

    def summarize(self, text, sentences=8):
        """
        Generate an extractive summary.
        """

        parser = PlaintextParser.from_string(
            text,
            Tokenizer("english")
        )

        summarizer = LsaSummarizer()

        summary = summarizer(
            parser.document,
            sentences
        )

        return [str(sentence) for sentence in summary]

    def keywords(self, text, top_n=20):
        """
        Extract keywords using YAKE.
        """

        extractor = yake.KeywordExtractor()

        keywords = extractor.extract_keywords(text)

        return keywords[:top_n]