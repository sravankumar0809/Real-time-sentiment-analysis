import pandas as pd
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
print("Loading dataset...")
data = load_files('aclImdb/train', categories=['pos', 'neg'], encoding='utf-8')

# Create a DataFrame
df = pd.DataFrame({'review': data.data, 'sentiment': data.target})

# (Optional) Map 0 -> 'Negative' and 1 -> 'Positive'
df['sentiment'] = df['sentiment'].map({0: 'Negative', 1: 'Positive'})

# Inspect few samples
print(df.head())

# Split the dataset into features and labels
X = df['review']    # Feature: the review text
y = df['sentiment'] # Label: the sentiment

# Split the data into training and validation sets (80% train, 20% validation)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline: Tfidf + SVC
model_pipeline = make_pipeline(
    TfidfVectorizer(stop_words='english'),  # TF-IDF Vectorizer
    SVC(kernel='linear')                    # Linear Support Vector Classifier
)

# Train the model
print("Training model...")
model_pipeline.fit(X_train, y_train)

# Validate the model
print("Validating model...")
y_pred = model_pipeline.predict(X_val)
accuracy = accuracy_score(y_val, y_pred)
print(f'Model validation accuracy: {accuracy:.4f}')

# Save the model
joblib.dump(model_pipeline, 'trained_imdb_svc_model.pkl')
print("Model training complete and saved as 'trained_imdb_svc_model.pkl'.")
