import re
import string
import nltk
from nltk.tokenize import RegexpTokenizer
<<<<<<< HEAD
from nltk.corpus import stopwords

# Download necessary NLTK resources (if not already downloaded)
nltk.download('stopwords', quiet=True)

# Stopwords set
STOPWORDS = set(stopwords.words('english'))

# Tokenizer to extract words (ignores punctuation)
tokenizer = RegexpTokenizer(r'\w+')

def preprocess_user_input(text: str) -> str:
    """
    Clean the text:
    - Lowercase
    - Remove URLs, mentions, numbers, punctuation
    - Tokenize and remove stopwords
    - Return cleaned text
    """
    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)

    # Remove mentions and hashtags
    text = re.sub(r'@\w+|#\w+', '', text)
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize
    tokens = tokenizer.tokenize(text)

    # Remove stopwords
    tokens = [tok for tok in tokens if tok not in STOPWORDS]

    # Join tokens
    cleaned_text = ' '.join(tokens)

    return cleaned_text
=======
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

nltk.download("stopwords")

from nltk.corpus import stopwords

# Define the list of stopwords
stopwordlist = [
    'a', 'about', 'above', 'after', 'again', 'ain', 'all', 'am', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because',
    'been', 'before', 'being', 'below', 'between', 'both', 'by', 'can', 'd', 'did', 'do', 'does', 'doing', 'down',
    'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers',
    'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'just', 'll', 'm',
    'ma', 'me', 'more', 'most', 'my', 'myself', 'now', 'o', 'of', 'on', 'once', 'only', 'or', 'other', 'our', 'ours',
    'ourselves', 'out', 'own', 're', 's', 'same', 'she', "shes", 'should', "shouldve", 'so', 'some', 'such', 't',
    'than', 'that', "thatll", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this',
    'those', 'through', 'to', 'too', 'under', 'until', 'up', 've', 'very', 'was', 'we', 'were', 'what', 'when', 'where',
    'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'won', 'y', 'you', "youd", "youll", "youre", "youve", 'your',
    'yours', 'yourself', 'yourselves'
]

# Initialize the tokenizer and the vectorizer
tokenizer = RegexpTokenizer('\s+', gaps=True)
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=5000)

# Function for preprocessing user input
def preprocess_user_input(user_input):
    # Apply the same preprocessing steps as in the code you provided
    # Convert to lowercase if user_input is a string
    if isinstance(user_input, str):
       user_input = user_input.lower()
    
    # Convert to lowercase
    user_input = user_input.lower()

    # Remove stopwords
    user_input = ' '.join([word for word in user_input.split() if word not in stopwordlist])

    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    user_input = user_input.translate(translator)

    # Remove repeating characters
    user_input = re.sub(r'(.)1+', r'1', user_input)

    # Remove URLs
    user_input = re.sub('((www.[^s]+)|(https?://[^s]+))', ' ', user_input)

    # Remove numeric numbers
    user_input = re.sub('[0-9]+', '', user_input)

    # Tokenization
    user_input = tokenizer.tokenize(user_input)

    # Lemmatization (Optional, you can uncomment if needed)
    # user_input = [lm.lemmatize(word) for word in user_input]
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    # Vectorize user input using the same vectorizer as in your code
    user_input = vectorizer.transform(user_input)

    return user_input

# Example of how to use the function:
user_input = "Hello, my name is Gaurav. I am very happy today!"
preprocessed_input = preprocess_user_input(user_input)
print(preprocessed_input)
>>>>>>> a4ed8ab (initial files)
