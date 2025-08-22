# EchoTags

[![Python](https://img.shields.io/badge/Python-blue)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-green)](https://flask.palletsprojects.com)
[![NLP](https://img.shields.io/badge/NLP-spaCy%20%7C%20NLTK-orange)](https://spacy.io/)
[![TF-IDF](https://img.shields.io/badge/Text-Vectorization-yellow)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)

---

## Overview

EchoTags is a web application that generates hashtags from text or PDF documents using Natural Language Processing (NLP). It leverages **spaCy** for Named Entity Recognition (NER), **NLTK** for stopword handling, and **TF-IDF vectorization** from scikit-learn to extract meaningful keywords and convert them into hashtags.

The project is designed with a clean and responsive UI using HTML, CSS, and JavaScript to make hashtag generation intuitive and interactive.

---

## Features

- Generate hashtags from text input or uploaded PDFs.
- Highlight detected keywords within the input text.
- Copy individual or all hashtags with a single click.
- Simple and modern user interface.

---

## Directory Structure

```
echo-tags
│
├── static
│   └── style.css                # Styling for the web app
│
├── templates
│   └── index.html               # Main HTML template (HTML + JS integration)
│
├── hashtag_generator.py         # Core NLP + hashtag generation logic
├── app.py                       # Flask web application
└── requirements.txt             # Python dependencies
```

---

## Installation

1. Clone the repository

```bash
git clone https://github.com/tayyabalitech/echo-tags.git
cd echo-tags
```

2. Create a virtual environment (optional but recommended)

For Linux/macOS:
```bash
python -m venv venv
source venv/bin/activate
```

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

1. Run the Flask app

```bash
python app.py
```

2. Open your browser and go to:
```
http://127.0.0.1:5000
```

3. Enter text or upload a PDF file.

4. Click **Generate Hashtags** to view and copy results.

---

## Technologies Used

- Python 3
- Flask for web framework
- spaCy for Named Entity Recognition
- NLTK for stopword processing
- scikit-learn for TF-IDF keyword extraction
- pdfplumber for PDF text extraction
- HTML, CSS, and JavaScript for frontend design

---

## Contact

📧 Contact  
For questions, suggestions, or collaborations, feel free to reach out

- GitHub [tayyabalitech](https://github.com/tayyabalitech)  
- LinkedIn [tayyabalitech](https://www.linkedin.com/in/tayyabalitech)  
- Email [tayyabalitechpro@gmail.com](mailto:tayyabalitechpro@gmail.com)

---

## Made with ❤️ by Tayyab Ali

