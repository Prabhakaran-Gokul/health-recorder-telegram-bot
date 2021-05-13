import requests
import json
import os

class Credentials:
    def __init__(self):
        self.bot_token = None
        self.URL = "https://health-recorder-app.herokuapp.com/"
        self.DB_URL = None
    
    def get_token(self):
        return self.bot_token

    def set_localhost(self, localhost):
        self.URL = localhost

    def get_URL(self):
        return self.URL

    def get_DB_URL(self):
        return self.DB_URL

    def set_token(self, token):
        self.bot_token = token

    def set_DB_URL(self, DB_URL):
        self.DB_URL = DB_URL

    def retrieve_credentials(self):
        # config_var_url = "https://api.heroku.com/apps/health-recorder-app/config-vars"
        # headers = {'Accept': 'application/vnd.heroku+json; version=3'}
        # response = requests.get(config_var_url, headers=headers)
        # json_data = json.loads(response.text) 
        # self.set_token(json_data["BOT_TOKEN"])
        # self.set_DB_URL(json_data["DB_URL"])
        self.set_token(os.environ['BOT_TOKEN'])
        self.set_DB_URL(os.environ['DB_URL'])
