"""Simple in-memory knowledge base for UPSC chatbot."""

from difflib import get_close_matches
from typing import Dict


class KnowledgeBase:
    """A minimal key-value knowledge store with fuzzy search."""

    def __init__(self, data: Dict[str, str]):
        self.data = {k.lower(): v for k, v in data.items()}

    def search(self, query: str) -> str:
        """Return the best matching answer or a default message."""
        query = query.lower().strip()
        if query in self.data:
            return self.data[query]
        matches = get_close_matches(query, self.data.keys(), n=1, cutoff=0.6)
        if matches:
            return self.data[matches[0]]
        return (
            "I'm sorry, I don't have an answer for that. "
            "Please ask about the UPSC exam or syllabus."
        )


DEFAULT_DATA = {
    "what is upsc prelims": (
        "The UPSC Preliminary Exam is the first stage of the Civil Services "
        "Examination. It consists of two objective papers of 200 marks each "
        "(General Studies I and General Studies II)."
    ),
    "what is upsc mains": (
        "The UPSC Main Exam is the second stage and includes nine papers: "
        "Essay, four General Studies papers, two optional subject papers, and "
        "language papers."
    ),
    "what are eligibility criteria": (
        "Candidates must be citizens of India, aged 21–32 (with category "
        "relaxations), and hold at least a bachelor's degree."
    ),
}

kb = KnowledgeBase(DEFAULT_DATA)
