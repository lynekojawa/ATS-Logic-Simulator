"""
constants.py
Dedicated registry for fluff words, STEM exceptions, and string conversions.
"""

GAME_JD_FLUFF = {
    "game", "games", "gaming", "play", "player", "players", "fun", "studio",
    "studios", "team", "teams", "work", "working", "join", "opportunity"
}

HR_LEGAL_FLUFF = {
    "equal", "opportunity", "employer", "race", "color", "religion", "sex",
    "national", "origin", "disability", "protected", "veteran", "status",
    "sexual", "orientation", "gender", "identity", "applicant", "applicants"
}

STOP_WORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and",
    "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being",
    "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't",
    "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during",
    "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't",
    "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here",
    "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i",
    "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's",
    "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself",
    "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought",
    "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
    "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such",
    "than", "that", "that's", "the", "their", "theirs", "them", "themselves",
    "then", "there", "there's", "these", "they", "they'd", "they'll", "they're",
    "they've", "this", "those", "through", "to", "too", "under", "until", "up",
    "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were",
    "weren't", "what", "what's", "when", "when's", "where", "where's", "which",
    "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would",
    "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
    "yourself", "yourselves"
}

STOP_WORDS.update(GAME_JD_FLUFF)
STOP_WORDS.update(HR_LEGAL_FLUFF)

STEM_EXCLUSION = {
    "analysis", "analytics", "bias", "calculus", "corpus", "census",
    "status", "process", "success", "access", "physics", "mathematics",
    "statistics", "focus", "class", "address", "addressing", "alias",
    "atlas", "canvas", "chaos", "crisis", "electronics", "ethics", "gas",
    "glass", "graphics", "hypothesis", "iris", "lens", "loss", "mass",
    "minus", "pass", "plus", "progress", "radius", "stress", "thesis",
    "witness", "wellness", "fitness", "languages", "database", "expertise",
    "compliance", "governance", "aws", "os", "ios", "macos", "jenkins",
    "pandas", "keras", "redis", "postgres", "kubernetes", "business",
    "businesses", "technology", "technologies", "series", "species"
}

WORD_TO_NUM = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10"
}