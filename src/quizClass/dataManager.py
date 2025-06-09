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
                    f.write("")

    # Generic loading function
    def load(self, _resource):
        if _resource not in self.INPUT_FILES.keys():
            raise Exception("Requested to load a file that do not exists")
        if not os.path.exists(self.INPUT_FILES.get(_resource)):
            return []
        with open(self.INPUT_FILES.get(_resource), 'r', encoding='utf-8') as f:
            return json.load(f)
    
    # Usefull for load resultst
    def loadTxtOutput(self, _resource):
        if _resource not in self.OUTPUT_FILES.keys():
            raise Exception("Requested to load a file that do not exists")
        if not os.path.exists(self.OUTPUT_FILES.get(_resource)):
            return []
        with open(self.OUTPUT_FILES.get(_resource), 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        if not lines:
            return []
        return lines

    def saveJson(self, _resource, _content):
        if _resource not in self.OUTPUT_FILES.keys():
            raise Exception("Requested to load a file that do not exists")
        if os.path.exists(self.OUTPUT_FILES.get(_resource)):
            with open(self.OUTPUT_FILES.get(_resource), 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    if not isinstance(data, list):  # Ensure data is a list, added becouse if json file is empty "{}" it will generate a dictionary
                        data = []
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        data.append(_content)

        with open(self.OUTPUT_FILES.get(_resource), 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    
    def saveTxt(self, _resource, _content):
        if _resource not in self.OUTPUT_FILES.keys():
            raise Exception("Requested to load a file that do not exists")
        with open(self.OUTPUT_FILES.get(_resource), 'a', encoding='utf-8') as f:
            f.write(json.dumps(_content, ensure_ascii=False) + "\n")

    def overwriteInput(self, _resource, _content):
        if _resource not in self.INPUT_FILES.keys():
            raise Exception("Requested to load a file that do not exists")
        with open(self.INPUT_FILES.get(_resource), 'w', encoding='utf-8') as f:
            json.dump(_content, f, indent=4, ensure_ascii=False)

    # Load topics from file
    def load_topics(self):
        return self.load("topics")