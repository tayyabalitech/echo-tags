import spacy
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import re

# 📥 Download NLTK stopwords
nltk.download('stopwords')

# ⚙️ Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

stop_words = set(stopwords.words('english'))

def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text).strip()

def format_hashtag(term):
    term = clean_text(term)
    if not term or len(term) <= 1:
        return None
    return '#' + ''.join(word.capitalize() for word in term.split() if word.isalnum())

def extract_keywords_with_tfidf(text, top_n=10):
    doc = nlp(text)
    words = [
        token.lemma_.lower()
        for token in doc
        if token.pos_ in {"NOUN", "PROPN", "ADJ"}
        and token.text.lower() not in stop_words
        and token.is_alpha
    ]
    if not words:
        return []
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform([" ".join(words)])
    idf_scores = tfidf.idf_
    terms = tfidf.get_feature_names_out()
    word_score_pairs = list(zip(terms, idf_scores))
    sorted_keywords = sorted(word_score_pairs, key=lambda x: x[1])[:top_n]
    return [kw for kw, _ in sorted_keywords]

def generate_hashtags(text):
    doc = nlp(text)
    keywords = set()

    # Named Entities
    for ent in doc.ents:
        if ent.label_ not in ['DATE', 'TIME', 'PERCENT', 'MONEY', 'QUANTITY', 'ORDINAL', 'CARDINAL']:
            cleaned_ent = clean_text(ent.text)
            if cleaned_ent and cleaned_ent.lower() not in stop_words:
                keywords.add(cleaned_ent)

    # TF-IDF keywords
    tfidf_keywords = extract_keywords_with_tfidf(text)
    keywords.update(tfidf_keywords)

    # Format into hashtags
    formatted_keywords = [format_hashtag(kw) for kw in keywords]
    formatted_keywords = [tag for tag in formatted_keywords if tag and len(tag) > 1]

    # Remove duplicates while preserving order
    seen = set()
    filtered_hashtags = []
    for tag in formatted_keywords:
        if tag not in seen:
            filtered_hashtags.append(tag)
            seen.add(tag)

    return filtered_hashtags[:10]  # Top 10
