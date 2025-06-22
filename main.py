from flask import Flask, render_template, request, redirect, url_for
import joblib
from data_preprocessing import preprocess_user_input

app = Flask(__name__)

# Load the trained model pipeline (already includes vectorizer and SVC)
model = joblib.load('trained_imdb_svc_model.pkl')

def split_opinions(file_content: str):
    """
    Split text into individual opinions:
    One opinion per line.
    """
    lines = file_content.strip().splitlines()
    opinions = [line.strip() for line in lines if line.strip()]  # Ignore empty lines
    return opinions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    uploaded = request.files.get('file')
    if not uploaded or uploaded.filename == '':
        return redirect(url_for('index'))

    # Read the uploaded file content
    raw = uploaded.read().decode('utf-8')
    
    # Split into individual opinions (1 review per line)
    opinions = split_opinions(raw)

    pos_count = 0
    neg_count = 0

    for op in opinions:
        # Preprocess each opinion
        clean = preprocess_user_input(op)
        
        # Predict sentiment
        pred = model.predict([clean])[0]
        
        if pred == 'Positive':
            pos_count += 1
        else:
            neg_count += 1

    return render_template('analysis.html',
                           total=len(opinions),
                           positive=pos_count,
                           negative=neg_count)

if __name__ == '__main__':
    app.run(debug=True)
