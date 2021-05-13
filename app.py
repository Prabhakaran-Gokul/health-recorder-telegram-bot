from flask import Flask, request
import telegram 
from datetime import datetime
from firebase import firebase

from Credentials import Credentials
from Storage import Storage
from Reminder import Reminder

global bot 
global TOKEN


credentials = Credentials()
credentials.retrieve_credentials()
# credentials.set_localhost("https://a1d689076565.ngrok.io/")

storage = Storage()
storage.authenticate(credentials.get_DB_URL())

TOKEN = credentials.get_token() 
bot = telegram.Bot(token=TOKEN)

reminder = Reminder(bot, storage)
reminder.start_scheduler()


# start flask app 
app = Flask(__name__)

@app.route("/{}".format(TOKEN), methods = ['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    data = request.get_json(force=True)
    print ("Received json data: \n{}".format(data))
    if data == None:
        return "Data received as None"
    update = telegram.Update.de_json(data, bot)
    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    timestamp = update.message.date

    text = update.message.text.encode('utf-8').decode()
    print ("Received text message: ", text)
    if text == "/start":
        bot_welcome = "hello there!"
        bot.sendMessage(chat_id = chat_id, text = bot_welcome, reply_to_message_id = msg_id)
    elif isValidValue(text):
        value_recorded = "You have recorded a blood glucose level of {}".format(text)
        bot.sendMessage(chat_id = chat_id, text = value_recorded, reply_to_message_id = msg_id)
        data = format_data_to_dict(float(text), datetime.timestamp(timestamp))
        storage.insert_record("Patient", chat_id, data)
    else:
        unknown_message = "Sorry I do not recognise that.\n\nTo submit your blood glucose level, type in your reading (in mmol/L), e.g. 7.3"
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

# def insert_record_to_db(user_type, chat_id, data):
#     fb = firebase.FirebaseApplication(credentials.get_DB_URL(), None)
#     result = fb.post(user_type + '/' + str(chat_id), data)



@app.route("/set_webhook", methods = ["GET", "POST"])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=credentials.get_URL(), HOOK=TOKEN))
    if s:
        return "Webhook setup ok"
    else:
        return "Webhook setup failed"
    
@app.route('/')
def index():
    return '.'

if __name__ == "__main__":
    app.run(threaded = True)
    