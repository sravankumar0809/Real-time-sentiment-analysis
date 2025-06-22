import re
import string
import nltk
from nltk.tokenize import RegexpTokenizer
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
