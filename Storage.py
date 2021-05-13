from uuid import NAMESPACE_X500
from firebase import firebase
from werkzeug.wrappers import StreamOnlyMixin

class Storage:
    def __init__(self):
        self.fb = None

    def authenticate(self, DB_URL):
        self.fb = firebase.FirebaseApplication(DB_URL, None)

    def insert_record(self, user_type, chat_id, data):
        if self.fb == None: 
            return "Database not authenticated"
        result = self.fb.post(user_type + '/' + str(chat_id), data)

    def get_chat_ids(self, user_type):
        data = self.fb.get(user_type, None)
        return list(data.keys())
