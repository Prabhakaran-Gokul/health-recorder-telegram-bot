import matplotlib.pyplot as plt
from datetime import datetime
import os 

class Statistics:
    def __init__(self, storage):
        self.storage = storage
        self.temp_folder = "tmp"
        if not os.path.isdir(self.temp_folder):
            os.mkdir("./{}/".format(self.temp_folder))

    def generate_graph(self, chat_id):
        #get values for the x and y axis
        glucose_levels = self.storage.get_glucose_levels("Patient", chat_id)
        timestamps = self.storage.get_timestamps("Patient", chat_id)
        formatted_timestamps = self.format_timestamps(timestamps)

        #plot and save graph
        fig, ax = plt.subplots()
        ax.scatter(formatted_timestamps, glucose_levels)
        ax.plot(formatted_timestamps, glucose_levels, '-o')
        ax.set_ylim(bottom=0)
        ax.set_ylabel("Glucose Level")
        ax.set_xlabel("Time")
        plt.title("Glucose levels vs Time")
        plt.gcf().autofmt_xdate()

        fig.savefig("{}/{}.png".format(self.temp_folder, chat_id))
        return "{}/{}.png".format(self.temp_folder, chat_id)

    #convert timestamp to datetime object
    def format_timestamps(self, timestamps):
        formatted_timestamps = []
        for timestamp in timestamps:
            dt_object = datetime.fromtimestamp(timestamp)
            formatted_timestamps.append(dt_object)
        return formatted_timestamps