from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
app = Flask(__name__)

english_bot = ChatBot("Kookie", read_only = True,                  
                 preprocessors=['chatterbot.preprocessors.clean_whitespace',
                 'chatterbot.preprocessors.unescape_html',
                 'chatterbot.preprocessors.convert_to_ascii'],                 
                storage_adapter = "chatterbot.storage.SQLStorageAdapter")
trainer = ListTrainer(english_bot)
conversation = [
    "Hello",
    "Hello!!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    'What is your name?', 
    'My name is Kookie.I am built by using python',
    'Bye?', 
    'Bye, see you later'
]
trainer.train(conversation)
trainer_corpus = ChatterBotCorpusTrainer(english_bot)
trainer_corpus.train('chatterbot.corpus.english')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
