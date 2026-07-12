# app/intelligence/constants.py


COMMON_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "by",
    "for",
    "from",
    "has",
    "have",
    "he",
    "i",
    "if",
    "in",
    "is",
    "it",
    "its",
    "me",
    "my",
    "of",
    "on",
    "or",
    "our",
    "she",
    "so",
    "that",
    "the",
    "their",
    "them",
    "there",
    "they",
    "this",
    "to",
    "was",
    "we",
    "were",
    "will",
    "with",
    "you",
    "your",
}

DOMAIN_STOPWORDS = {

    "app",
    "apps",
    "application",

    "google",
    "play",

    "please",

    "would",

    "really",

    "very",

    "just",

    "like",
}

STOPWORDS = COMMON_STOPWORDS | DOMAIN_STOPWORDS