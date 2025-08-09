import nltk
import random
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm a chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good\nHow about You?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
    ],
    [
        r"what (.*) want?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created you?",
        ["I was created by a human.",]
    ],
    [
        r"(.*) (location|city)?",
        ['I am everywhere',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1", "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an amazing company, I have heard about it.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2", "Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I am a computer program, so I am always healthy ",]
    ],
    [
    r"quit",
    ["Bye! Have a great day.", "Goodbye!"]
]

]

# Create a Chatbot
def chatbot():
    print("Hi, I'm Chatbot! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    # The user may need to download the 'punkt' model
    try:
        nltk.data.find('tokenizers/punkt')
    except nltk.downloader.DownloadError:
        print("Downloading 'punkt' model...")
        nltk.download('punkt')
        print("Download complete.")

    chatbot()
