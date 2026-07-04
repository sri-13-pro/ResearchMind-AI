"""
===========================================================
Text Preprocessing Functions
AI Research Paper Intelligence System
===========================================================
"""

import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download resources (only first time)
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    """
    Basic text cleaning.
    """

    text = text.lower()

    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def tokenize(text):
    """
    Tokenize text into words.
    """

    return word_tokenize(text)


def remove_stopwords(tokens):
    """
    Remove stopwords.
    """

    return [
        word
        for word in tokens
        if word not in stop_words
    ]


def lemmatize(tokens):
    """
    Lemmatize tokens.
    """

    return [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]


def preprocess(text):
    """
    Complete preprocessing pipeline.
    """

    text = clean_text(text)

    tokens = tokenize(text)

    tokens = remove_stopwords(tokens)

    tokens = lemmatize(tokens)

    return tokens


def text_statistics(text):
    """
    Return text statistics.
    """

    words = word_tokenize(text)

    stats = {
        "Characters": len(text),
        "Words": len(words),
        "Unique Words": len(set(words)),
        "Sentences": len(re.split(r"[.!?]", text))
    }

    return stats