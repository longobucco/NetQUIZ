import os
import json
import src.quizClass.utility as util

class DataManager(object):
    INPUT_FILES = {
        "quiz": util.QUIZ_FILE,
        "topics": util.ARGOMENTI_FILE
    }

    OUTPUT_FILES = {
        "results": util.RESULTS_FILE,
        "progress": util.PROGRESS_FILE,
        "stats": util.STATS_FILE
    }

    def __init__(self):
        for filename in self.OUTPUT_FILES.values():
            if not os.path.exists(filename):
                with open(filename, "w") as f:
                    json.dump({}, f)

    # Generic loading function
    def load(self, resurce):
        if resurce not in self.INPUT_FILES.keys():
            raise Exception("Requested to load a file that do not exists")
        if not os.path.exists(self.INPUT_FILES.get(resurce)):
            return []
        with open(self.INPUT_FILES.get(resurce), 'r', encoding='utf-8') as f:
            return json.load(f)

    #def save(self, resource):





    # Load topics from file
    def load_topics(self):
        return self.load("topics")