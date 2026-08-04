"""
constants.py
Dedicated registry for fluff words, STEM exceptions, and string conversions.
"""

GOVERNMENT_NOISE = {
    "agency", "department", "federal", "government", "official", "office",
    "management", "command", "directorate", "installation", "garrison", "service",
    "services", "civilian", "competitive", "position", "positions", "announcement",
    "summary", "overview", "organization", "program", "programs", "mission",
    "authority", "authorities", "administration", "administrative", "public", "national",
    "state", "states", "province", "provincial", "city", "local", "communities",
    "community", "location", "locations", "site", "worksite", "overseas", "oconus",
    "domestic", "foreign", "republic", "embassy"
}

LEGAL_NOISE = {
    "accordance", "applicable", "eligibility", "eligible", "requirements", "requirement",
    "required", "determination", "provisions", "provision", "regulation", "regulations",
    "instruction", "instructions", "policy", "policies", "compliance", "comply",
    "maintain", "maintained", "obtain", "obtaining", "subject", "condition",
    "conditions", "authorization", "authorized", "qualify", "qualified", "qualification",
    "qualifications", "documentation", "document", "documents", "proof", "criteria",
    "selectee", "selected", "assessment", "assess", "review", "reviews",
    "annual", "periodic", "duration"
}

RECRUITING_NOISE = {
    "apply", "application", "applications", "applicant", "applicants", "appointment",
    "appointments", "promotion", "promotions", "reassignment", "reassignments", "employment",
    "employee", "employees", "employer", "career", "careers", "hiring", "hire",
    "recruitment", "retention", "transition", "consideration", "considered", "vacancy",
    "vacancies", "resume", "questionnaire", "interview", "candidate", "candidates",
    "selection", "score", "referred", "manager", "supervisory", "probation", "grade",
    "grades", "schedule", "series"
}

BENEFITS_NOISE = {
    "salary", "benefits", "allowance", "allowances", "expenses", "expense",
    "reimbursement", "travel", "telework", "remote", "deposit", "pay", "payment",
    "payments", "leave", "quarters", "passport", "incentive", "incentives", "loan",
    "repayment", "package", "packages", "hours", "hour", "fulltime", "parttime",
    "permanent", "temporary"
}

HR_POLICY_NOISE = {
    "complaints", "complaint", "grievance", "grievances", "guidance", "advice",
    "counsel", "performance", "appraisal", "supervisor", "supervisors", "staff",
    "staffing", "personnel", "person", "persons", "member", "members", "family",
    "spouse", "spouses", "dependent", "dependents", "veteran", "veterans", "citizenship",
    "citizen", "registration", "employment", "employments", "return", "rights",
    "supporting", "support", "supports"
}

DOCUMENT_NOISE = {
    "website", "url", "online", "click", "access", "visit", "information",
    "additional", "details", "detail", "notice", "section", "pages", "page",
    "response", "responses", "form", "report", "reports", "statement", "statements",
    "address", "contact", "contacts", "questions", "question", "include", "including",
    "provided", "provide", "provides", "submitted", "submit", "submission", "receive",
    "received", "receives", "complete", "completed"
}

LOCATION_NOISE = {
    "south", "korea", "seoul", "pyongtaek", "humphreys", "apo", "area", "areas",
    "country", "countries", "location", "locations", "drive", "travel", "overseas",
    "abroad", "foreign", "base", "bases", "installation", "headquarters"
}


ACTION_VERB_NOISE = {
    "coordination", "coordinating", "planning", "plans", "managing", "manages",
    "directing", "directs", "evaluating", "evaluation", "responsible", "responsibility",
    "assigned", "assignment", "functions", "operations", "resources", "current",
    "future", "quality", "effective", "efficient", "ensure", "ensures", "maintains",
    "establishes", "develops", "implements", "performs", "serves", "include", "includes"
}


TECHNICAL_NOISE = {
    "data", "source", "customer", "cloud", "build", "open", "system",
    "related", "including", "solution", "tool", "using", "experience"
}

JOB_META_FLUFF = {
    "year", "years", "none", "preferred", "manager", "minimum", "direct",
    "qualification", "position", "hiring", "staffing", "paid", "professional",
    "support", "help", "detail", "will", "careerscape", "ll", "re", "thi" # thi, re, ll 같은 유령 어근 추가
}

CYBER_DOMAIN_NOISE = {
    "risk", "management", "governance", "cybersecurity", "financial",
    "regulatory", "cyber", "chainguard", "alpaca"
}

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

STOP_WORDS.update(GOVERNMENT_NOISE)
STOP_WORDS.update(LEGAL_NOISE)
STOP_WORDS.update(RECRUITING_NOISE)
STOP_WORDS.update(BENEFITS_NOISE)
STOP_WORDS.update(HR_POLICY_NOISE)
STOP_WORDS.update(DOCUMENT_NOISE)
STOP_WORDS.update(LOCATION_NOISE)
STOP_WORDS.update(ACTION_VERB_NOISE)
STOP_WORDS.update(TECHNICAL_NOISE)
STOP_WORDS.update(JOB_META_FLUFF)
STOP_WORDS.update(CYBER_DOMAIN_NOISE)
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