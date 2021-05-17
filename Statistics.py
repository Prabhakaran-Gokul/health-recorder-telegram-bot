import matplotlib.pyplot as plt
from datetime import datetime

class Statistics:
    def __init__(self, storage):
        self.storage = storage

    def generate_graph(self, chat_id):
        #get values for the x and y axis
        glucose_levels = self.storage.get_glucose_levels("Patient", chat_id)
        timestamps = self.storage.get_timestamps("Patient", chat_id)
        formatted_timestamps = self.format_timestamps(timestamps)

        #plot and save graph
        plt.scatter(formatted_timestamps, glucose_levels)
        plt.plot(formatted_timestamps, glucose_levels, '-o')
        plt.gcf().autofmt_xdate()
        plt.savefig('{}.png'.format(chat_id))
        return "{}.png".format(chat_id)

    #convert timestamp to datetime object
    def format_timestamps(self, timestamps):
        formatted_timestamps = []
        for timestamp in timestamps:
            dt_object = datetime.fromtimestamp(timestamp)
            formatted_timestamps.append(dt_object)
        return formatted_timestamps