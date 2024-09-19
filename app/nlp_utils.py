from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter

def summarize_text(text, num_sentences=3):
    sentences = sent_tokenize(text)

    # Tokenize words and remove stopwords
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stop_words]
    # Get word frequency
    word_freq = Counter(words)
    # Rank sentences based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        sentence_words = word_tokenize(sentence.lower())
        sentence_score = sum(word_freq.get(word, 0) for word in sentence_words)
        sentence_scores[sentence] = sentence_score
    # Sort sentences by score and return the top ones
    ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    summary = ' '.join(ranked_sentences[:num_sentences])
    return summary

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)  
    if sentiment_scores['compound'] >= 0.05:
        sentiment = "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"    
    return sentiment


def list_unique_words(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stop_words]
    # Get word frequency
    word_freq = Counter(words)
    return word_freq.most_common()