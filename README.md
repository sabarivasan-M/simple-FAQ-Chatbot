


---



  FAQ Chatbot using NLP and Tkinter

This is a lightweight, desktop-based chatbot application that simulates FAQ interaction using Natural Language Processing and a Tkinter-powered GUI.

---

 Features

- Interactive chat interface
- Responds to known FAQ queries using NLP techniques
- Uses `nltk` for tokenization and `scikit-learn` for similarity checking
- Simple, responsive GUI layout
- Fallback response when a question is not understood



 GUI Preview

![Chatbot GUI]

![ChatGPT Image Jun 19, 2025, 12_18_10 PM](https://github.com/user-attachments/assets/396b6d16-2fe1-4e18-b742-bff18b60444e)# simple-FAQ-Chatbot

##  Requirements


Install dependencies with:

```bash
pip install nltk scikit-learn numpy
````

Download necessary NLTK data:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

##  How It Works

1. A dictionary of known FAQs is stored in the code.
2. When a user asks a question:

   * The input is tokenized and vectorized.
   * Cosine similarity is calculated against known questions.
   * If similarity ≥ 0.3, it returns the matching answer.
   * Otherwise, it politely says it doesn't understand.

---

## Run the App

```bash
python task2.py
```

---

##  File Structure

```
task2/
├── task2.py


├── README.md


└── A_screenshot_of_a_desktop_FAQ_Chatbot_application_.png
```

---

##  License

This project is licensed under the **MIT License**.

```


##  Author

Created with purpose and polish by [Sabarivasan](https://github.com/sabarivasan-M)


