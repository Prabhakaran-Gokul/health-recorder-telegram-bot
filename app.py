from flask import Flask, request
import telegram 
import requests
import time
from firebase import firebase

from credentials import bot_token, bot_user_name, URL, DB_URL

global bot 
global TOKEN
TOKEN = bot_token 
bot = telegram.Bot(token=TOKEN)


# start flask app 
app = Flask(__name__)

@app.route("/{}".format(TOKEN), methods = ['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    text = update.message.text.encode('utf-8').decode()
    print ("Received text message: ", text)
    if text == "/start":
        bot_welcome = "hello there!"
        bot.sendMessage(chat_id = chat_id, text = bot_welcome, reply_to_message_id = msg_id)
    elif isValidValue(text):
        value_recorded = "You have recorded a glood glucose level of {}".format(text)
        bot.sendMessage(chat_id = chat_id, text = value_recorded, reply_to_message_id = msg_id)
        data = format_data_to_dict(float(text), time.time())
        insert_record_to_db("Patient", chat_id, data)
    else:
        unknown_message = "Sorry I do not recognise that.\n\nTo submit your glucose, type in your reading (in mg/dL), e.g. 120."
        bot.sendMessage(chat_id = chat_id, text = unknown_message, reply_to_message_id = msg_id)

    return "response ok"

def isValidValue(text):
    try:
        value = float(text)
    except (ValueError, TypeError):
        return False
    return True

def format_data_to_dict(value, timestamp):
    data = {
        "timestamp":timestamp,
        "glucose_level": value
    }
    return data

def insert_record_to_db(user_type, chat_id, data):
    fb = firebase.FirebaseApplication(DB_URL, None)
    result = fb.post(user_type + '/' + str(chat_id), data)



@app.route("/set_webhook", methods = ["GET", "POST"])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    # s = requests.get("https://api.telegram.org/bot{}/setWebhook?url={}".format(TOKEN, URL))
    if s:
        return "Webhook setup ok"
    else:
        return "Webhook setup failed"
    
@app.route('/')
def index():
    return '.'

if __name__ == "__main__":
    app.run(threaded = True)
    # print(bot.get_me())