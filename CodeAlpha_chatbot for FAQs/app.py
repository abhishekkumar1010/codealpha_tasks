import streamlit as st
import pandas as pd
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Load FAQ data
data = pd.read_csv("faq.csv")

questions = data["Question"]
answers = data["Answer"]

stop_words = set(stopwords.words("english"))

# Text preprocessing
def preprocess(text):
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stop_words]
    return " ".join(words)

processed_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(processed_questions)

# Streamlit UI
st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")

st.title("🤖 FAQ Chatbot")
st.write("Ask any question related to the FAQ database.")

user_input = st.text_input("Enter your question")

if st.button("Ask"):

    if user_input.strip() == "":
        st.warning("Please enter a question.")

    else:

        processed_input = preprocess(user_input)

        input_vector = vectorizer.transform([processed_input])

        similarity = cosine_similarity(input_vector, question_vectors)

        index = similarity.argmax()

        score = similarity[0][index]

        if score > 0.30:
            st.success(answers[index])
        else:
            st.error("Sorry! I don't know the answer.")