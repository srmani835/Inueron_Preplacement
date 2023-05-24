"""
Q-1. Take any YouTube videos link and your task is to extract the comments from
that videos and store it in a csv file and then you need define what is most
demanding topic in that videos comment section
"""
#Ans:

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from gensim import models
from gensim.corpora import Dictionary

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Function to scrape comments from a YouTube video
def scrape_youtube_comments(video_url):
    response = requests.get(video_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the comments section using the class attribute
    comments_section = soup.find('ytd-comments', recursive=False)

    if comments_section is None:
        print("Comments section not found.")
        return []

    # Find the comment elements within the section
    comments = comments_section.find_all('yt-formatted-string', {'id': 'content-text'})
    comments_list = [comment.text for comment in comments]

    return comments_list

# Function to preprocess the comments
def preprocess_comments(comments):
    processed_comments = []

    for comment in comments:
        # Convert to lowercase
        comment = comment.lower()

        # Remove special characters, URLs, and non-alphanumeric characters
        comment = re.sub(r"[^a-zA-Z0-9\s]", "", comment)
        comment = re.sub(r"http\S+|www\S+", "", comment)

        # Tokenize comment into words
        words = word_tokenize(comment)

        # Remove stop words and perform stemming
        stop_words = set(stopwords.words('english'))
        stemmer = PorterStemmer()
        words = [stemmer.stem(word) for word in words if word not in stop_words]

        # Add processed comment if it contains terms
        if len(words) > 0:
            processed_comments.append(words)

    return processed_comments

# Function to perform topic modeling
def perform_topic_analysis(comments):
    # Create a dictionary from the comments
    dictionary = Dictionary(comments)

    # Create a corpus (bag of words) representation
    corpus = [dictionary.doc2bow(comment) for comment in comments]

    # Perform LDA topic modeling
    lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=10)

    # Get the dominant topic for each comment
    topics = []
    for comment in comments:
        topic = lda_model.get_document_topics(dictionary.doc2bow(comment), minimum_probability=0.2)
        dominant_topic = max(topic, key=lambda x: x[1])[0]
        topics.append(dominant_topic)

    return topics

# Function to save topics to a CSV file
def save_topics_to_csv(topics, csv_file):
    df = pd.DataFrame({'Topic': topics})
    df.to_csv(csv_file, index=False)
    print('Topics saved to', csv_file)

# Specify the YouTube video URL
video_url = 'https://youtu.be/reUZRyXxUs4'

# Scrape comments from the YouTube video
comments = scrape_youtube_comments(video_url)

# Preprocess the comments
preprocessed_comments = preprocess_comments(comments)

# Perform topic analysis if comments are available
if len(preprocessed_comments) > 0:
    # Perform topic analysis
    topics = perform_topic_analysis(preprocessed_comments)

    # Specify the CSV file path
    csv_file = 'topics.csv'

    # Save topics to a CSV file
    save_topics_to_csv(topics, csv_file)
else:
    print("No comments available for topic analysis.")