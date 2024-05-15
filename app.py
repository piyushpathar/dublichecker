from flask import Flask, render_template, request
from docx import Document

app = Flask(__name__)

def has_duplicate_lines(file):
    # Create a set to store unique lines
    unique_lines = set()
    # Create a list to store duplicate lines
    duplicate_lines = []

    # Open the .docx file
    doc = Document(file)

    # Iterate over paragraphs in the document
    for paragraph in doc.paragraphs:
        # Get the text of the paragraph without stripping whitespace
        line = paragraph.text

        # Check if the line is not empty
        if line:
            # Check if the line is already in the set of unique lines
            # If it is, it's a duplicate, so add it to the list of duplicate lines
            if line in unique_lines:
                duplicate_lines.append(line)
            else:
                # Otherwise, add the line to the set of unique lines
                unique_lines.add(line)

    return duplicate_lines

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    # Pass the file object to the function instead of its filename
    duplicates = has_duplicate_lines(file)
    return render_template('result.html', duplicates=duplicates)

if __name__ == '__main__':
    app.run(debug=True)

