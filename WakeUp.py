from apscheduler.schedulers.background import BlockingScheduler
import requests
import os
import logging

class WakeUp:
    def __init__(self, app_url):
        self.app_url = app_url

    def wake_up_app(self):
        response = requests.get(url = self.app_url)
        logging.info("Request to app url with the status code: {}".format(response.status_code))

    def start_scheduler(self):
        #setting timezone to singapore
        scheduler = BlockingScheduler(timezone ="Asia/Singapore")
        scheduler.add_job(self.wake_up_app, 'cron', hour = '5,9', minute = 45)
        scheduler.add_job(self.wake_up_app, 'cron', hour = '15,18', minute = 45)
        scheduler.start()

if __name__ == "__main__":
    app_url = os.environ['APP_URL']
    wake_up = WakeUp(app_url)
    wake_up.start_scheduler()