from flask import Flask, request, render_template
from markupsafe import Markup
from hashtag_generator import generate_hashtags
import re
import pdfplumber
from io import BytesIO

# Initialize Flask app
app = Flask(__name__)

def extract_text_from_pdf(file_stream):
    """Extracts text content from a PDF file."""
    text = ""
    with pdfplumber.open(file_stream) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


@app.route('/', methods=['GET', 'POST'])
def index():
    hashtags = []
    highlighted_text = ""
    input_text = ""
    pdf_filename = None

    if request.method == 'POST':
        # If user uploads a PDF file
        if 'pdf_file' in request.files and request.files['pdf_file'].filename:
            file = request.files['pdf_file']
            pdf_filename = file.filename
            input_text = extract_text_from_pdf(BytesIO(file.read()))
        else:
            # Fallback: Get plain text from input field
            input_text = request.form.get('input_text', '')

        # Generate hashtags
        hashtags = generate_hashtags(input_text)

        # Highlight keywords in the original text
        raw_keywords = [tag[1:] for tag in hashtags]  # remove '#' symbol
        highlighted_text = input_text
        for word in sorted(raw_keywords, key=len, reverse=True):
            pattern = re.compile(r'\b(' + re.escape(word) + r')\b', re.IGNORECASE)
            highlighted_text = pattern.sub(r'<mark>\1</mark>', highlighted_text)

        highlighted_text = Markup(highlighted_text)  # Mark safe for HTML

    return render_template(
        'index.html',
        hashtags=hashtags,
        input_text=input_text,
        highlighted_text=highlighted_text,
        pdf_filename=pdf_filename
    )


if __name__ == '__main__':
    app.run(debug=True)
