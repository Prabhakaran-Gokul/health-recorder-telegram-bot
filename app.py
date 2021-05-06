from flask import Flask, request
import telegram 
from credentials import bot_token, bot_user_name, URL

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
        bot_welcome = "hello there"
        bot.sendMessage(chat_id = chat_id, text = bot_welcome, reply_to_message_id = msg_id)

    return "response ok"

@app.route("/set_webhook", methods = ["GET", "POST"])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
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