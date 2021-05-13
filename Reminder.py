from Storage import Storage
from apscheduler.schedulers.background import BackgroundScheduler

class Reminder:
    def __init__(self, bot, storage):
        self.bot = bot
        self.storage = storage
        self.reminder_message = ("Dear user, please key in your blood glucose "
        "reading (in mmol/L), e.g. 7.3")

    def send_reminder(self, chat_ids):
        for chat_id in chat_ids:
            self.bot.sendMessage(chat_id = chat_id, text = self.reminder_message)

    def start_scheduler(self):
        scheduler = BackgroundScheduler()
        chat_ids = self.storage.get_chat_ids("Patient")
        scheduler.add_job(self.send_reminder, 'cron', hour = 9, args=[chat_ids])
        scheduler.start()