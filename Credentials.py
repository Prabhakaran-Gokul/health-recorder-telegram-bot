import os

class Credentials:
    def __init__(self):
        self.bot_token = None
        self.URL = None
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

    def set_URL(self, URL):
        self.URL = URL

    def retrieve_credentials(self):
        self.set_token(os.environ['BOT_TOKEN'])
        self.set_DB_URL(os.environ['DB_URL'])
        self.set_URL(os.environ['APP_URL'])
