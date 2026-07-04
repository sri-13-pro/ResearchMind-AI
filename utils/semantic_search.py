"""
===========================================================
Semantic Search
ResearchMind AI
===========================================================
"""

import os
import pickle
import numpy as np
import faiss

from sentence_transformers import SentenceTransformer


def semantic_search():

    def __init__(self):

        print("Loading Sentence Transformer Model...")

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.index = None

    # -----------------------------------------------------

    def create_embeddings(self, dataframe):

        texts = (
            dataframe["title"].fillna("")
            + ". "
            + dataframe["abstract"].fillna("")
        ).tolist()

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True,
            convert_to_numpy=True
        )

        return embeddings

    # -----------------------------------------------------

    def build_index(self, embeddings):

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(
            embeddings.astype("float32")
        )

        print(f"Indexed {len(embeddings)} papers.")

    # -----------------------------------------------------

    def search(self, query, top_k=5):

        if self.index is None:
            raise Exception("Index has not been created.")

        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        )

        distances, indices = self.index.search(
            query_embedding.astype("float32"),
            top_k
        )

        return indices[0]

    # -----------------------------------------------------

    def save(self, folder="vector_db"):

        os.makedirs(folder, exist_ok=True)

        faiss.write_index(
            self.index,
            os.path.join(folder, "paper.index")
        )

        print("Vector Index Saved!")

    # -----------------------------------------------------

    def load(self, folder="vector_db"):

        path = os.path.join(folder, "paper.index")

        if os.path.exists(path):

            self.index = faiss.read_index(path)

            print("Vector Index Loaded!")

            return True

        return False
    