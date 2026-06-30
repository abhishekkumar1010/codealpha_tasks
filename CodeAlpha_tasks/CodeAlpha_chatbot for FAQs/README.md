# 🤖 FAQ Chatbot using NLP

A simple FAQ Chatbot built using **Python, NLTK, Scikit-learn, Pandas, and Streamlit**. The chatbot answers user questions by finding the most similar question in the FAQ dataset using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 📌 Project Objective

The objective of this project is to develop a chatbot that can automatically answer Frequently Asked Questions (FAQs) using Natural Language Processing (NLP) techniques.

---

## 🚀 Features

- Simple and user-friendly interface
- NLP-based text preprocessing
- TF-IDF Vectorization
- Cosine Similarity for question matching
- Fast and accurate responses
- Streamlit web interface

---

## 🛠 Technologies Used

- Python
- NLTK
- Pandas
- Scikit-learn
- Streamlit

---

## 📂 Project Structure

```
FAQ_Chatbot/
│
├── app.py
├── faq.csv
├── requirements.txt
└── README.md
```

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone <repository-link>
```

Or simply download the project folder.

### 2. Install the required libraries

```bash
pip install -r requirements.txt
```

### 3. Download NLTK data

```python
import nltk

nltk.download("punkt")
nltk.download("stopwords")
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

The chatbot will open automatically in your browser.

---

## 📄 Dataset

The chatbot uses a CSV file (`faq.csv`) containing two columns:

| Question | Answer |
|----------|--------|
| What is AI? | Artificial Intelligence is the simulation of human intelligence by machines. |
| What is Python? | Python is a high-level programming language. |

You can add more questions and answers to improve the chatbot.

---

## ⚙️ Working of the Chatbot

1. Load the FAQ dataset using Pandas.
2. Preprocess the text using NLTK.
3. Remove stopwords and punctuation.
4. Convert questions into numerical vectors using TF-IDF.
5. Convert the user's question into a TF-IDF vector.
6. Calculate Cosine Similarity between the user's question and stored questions.
7. Return the answer with the highest similarity score.
8. If no suitable match is found, display a default message.

---

## 📌 Example

**User:**

```
What is AI?
```

**Bot:**

```
Artificial Intelligence is the simulation of human intelligence by machines.
```

---

## 🎯 Future Enhancements

- Voice-based chatbot
- Chat history
- Database integration
- AI-powered responses using Large Language Models (LLMs)
- Multi-language support

---

## 👨‍💻 Developed By

**Name:** Abhishek Kumar

**Course:** B.Tech (AI & ML)

**College:** RVS College of Engineering and Technology, Jamshedpur

---

## 📜 License

This project is developed for educational and internship purposes only.