<<<<<<< HEAD
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
=======
from flask import Flask, redirect, render_template, request, jsonify, url_for
import tweepy
from textblob import TextBlob  # You can use your sentiment analysis model here
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from data_preprocessing import preprocess_user_input
app = Flask(__name__)

app.static_folder="static"

# Load the pre-trained TF-IDF vectorizer
# vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Load the pre-trained sentiment analysis model
sentiment_model = joblib.load('trained_model_svc.pkl')
>>>>>>> a4ed8ab (initial files)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
<<<<<<< HEAD
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
=======
    tweet_text = request.form['tweet']
    # print(tweet_text)
    # Preprocess the user input using the loaded vectorizer
    user_input = preprocess_user_input(tweet_text)

    # Predict sentiment using the loaded sentiment analysis model
    sentiment = sentiment_model.predict(user_input)
    
     # Check if any element in the sentiment array is 1 (positive)
    if any(sentiment == 1):
        sentiment_str = "Positive"
    # Check if any element in the sentiment array is -1 (negative)
    elif any(sentiment == -1):
        sentiment_str = "Negative"
    else:
        sentiment_str = "Neutral"
    # print(sentiment_str)
    return redirect(url_for('analysis', sentiment=sentiment_str))

@app.route('/analysis/<sentiment>')
def analysis(sentiment):
    return render_template('analysis.html', sentiment=sentiment)
if __name__ == '__main__':
    app.run()












# Set up Twitter API credentials (replace with your own credentials)
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Initialize Tweepy to access Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)



# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/analyze', methods=['POST'])
# def analyze():
#     tweet_text = request.form['tweet']
#     sentiment = perform_sentiment_analysis(tweet_text)
#     return sentiment

# # @app.route('/get_tweets')
# # def get_tweets():
# #     tweets = []
# #     for tweet in tweepy.Cursor(api.search, q='python', lang='en').items(10):
# #         tweet_data = {
# #             'text': tweet.text,
# #             'sentiment': perform_sentiment_analysis(tweet.text)
# #         }
# #         tweets.append(tweet_data)
# #     return jsonify(tweets)

# if __name__ == '__main__':
#     app.run()
>>>>>>> a4ed8ab (initial files)
