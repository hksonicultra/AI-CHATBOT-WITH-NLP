# AI-CHATBOT-WITH-NLP

# COMPANY: CODTECH IT SOLUTION

# NAME: Bhushan satyavan waghmare

# INTERN ID: CT04DH2105

# DOMAIN: PYTHON

# DURATION: 4 weeks

# MENTOR: NEELA SANTOSH



# 🗨️ Python NLTK Chatbot

## 📌 Overview

This project is a **simple rule-based chatbot** built using Python’s **NLTK** (Natural Language Toolkit) library.
It uses **pattern matching with regular expressions** to understand user input and respond accordingly.
Perfect for beginners learning about **Natural Language Processing (NLP)** and chatbot development.

---

## 🗂 Project Structure

```
.
├── chatbot.py       # Main chatbot script
└── README.md        # Project documentation
```

---

## ⚙️ How It Works

1. **Predefined Patterns**

   * User inputs are matched to predefined patterns using regex.
   * Responses are mapped to each pattern.

2. **Reflections**

   * The `reflections` dictionary automatically adjusts pronouns for more natural replies.

3. **NLTK Chat Utility**

   * The `Chat` class from `nltk.chat.util` handles pattern matching and conversation flow.

---

## 🛠 Requirements

Make sure you have:

* **Python 3.x**
* **pip** (Python package manager)

Install the required library:

```bash
pip install nltk
```

You may also need to download the NLTK `punkt` tokenizer:

```python
import nltk
nltk.download('punkt')
```

---

## 🚀 How to Run

1. **Run the Script**

   ```bash
   python chatbot.py
   ```
2. **Start Chatting**

   * Type your message and press Enter.
   * Type `quit` to exit.

---

## 💬 Example Chat

```
Hi, I'm Chatbot! Type 'quit' to exit.
You: hello
Bot: Hello

You: my name is John
Bot: Hello John, How are you today?

You: how are you?
Bot: I'm doing good
How about You?

You: quit
Bot: Goodbye!
```

---

## ✨ Features

* Rule-based chatbot with regex matching.
* Handles greetings, personal introductions, weather, company mentions, and more.
* Easy to customize with new patterns and replies.

---

## 📌 Customization

To add new responses:

1. Open `chatbot.py`.
2. Locate the `pairs` list.
3. Add a new pattern-response block:

```python
[
    r"do you like music?",
    ["Yes, I love music!", "Music makes me happy."]
]
```

4. Save and run again.

---

If you want, I can **also create a `requirements.txt`** for this chatbot so it’s ready for GitHub and installation in one command.
Do you want me to make that now?
