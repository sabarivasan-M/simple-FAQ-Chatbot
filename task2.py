# Simple FAQ Chatbot using NLTK and Tkinter

from tkinter import *
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

nltk.download('punkt')
nltk.download('stopwords')

# Sample FAQ Data
faq_data = {
    "What is your name?": "I am a chatbot created for FAQ support.",
    "How can I reset my password?": "Click on 'Forgot Password' and follow the instructions.",
    "What is the office timing?": "Our office timing is 9 AM to 6 PM.",
    "How to contact support?": "You can contact support via email or phone."
}

questions = list(faq_data.keys())
answers = list(faq_data.values())

# NLP Response Matching
def get_response(user_input):
    data = questions + [user_input]
    vect = CountVectorizer().fit_transform(data)
    cosine_sim = cosine_similarity(vect[-1], vect[:-1])
    index = np.argmax(cosine_sim)

    if cosine_sim[0, index] < 0.3:
        return "Sorry, I don't understand your question."
    else:
        return answers[index]

# GUI Part
def ask_bot():
    user_question = user_input.get()
    bot_response = get_response(user_question)
    chat_window.insert(END, f"You: {user_question}\n")
    chat_window.insert(END, f"Bot: {bot_response}\n\n")
    user_input.delete(0, END)

root = Tk()
root.title("FAQ Chatbot")
root.geometry("500x400")
root.configure(bg="#f2f2f2")

chat_window = Text(root, height=15, width=58)
chat_window.pack(pady=10)

user_input = Entry(root, width=50)
user_input.pack(side=LEFT, padx=10)

Button(root, text="Ask", command=ask_bot, bg="#4da6ff").pack(side=LEFT)

root.mainloop()