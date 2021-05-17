from firebase import firebase

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

    def get_timestamps(self, user_type, chat_id):
        timestamps = []
        data = self.fb.get(user_type, chat_id)
        for record in data.keys():
            timestamp = data[record]['timestamp']
            timestamps.append(timestamp)
        return timestamps

    def get_glucose_levels(self, user_type, chat_id):
        glucose_levels = []
        data = self.fb.get(user_type, chat_id)
        for record in data.keys():
            glucose_level = data[record]['glucose_level']
            glucose_levels.append(glucose_level)
        return glucose_levels
