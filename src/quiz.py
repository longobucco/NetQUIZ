import random
import time
from datetime import datetime
from src.quizClass.dataManager import DataManager
from src.quizClass.question import Question

import src.quizClass.utility as util

class Quiz(object):
    def __init__(self, _jsonQuiz):
        # future use, implement the possibility to print the question
        pass

    def  __init__(self):
        self.questions = []
        self.startTime = -1
        self.endTime = -1
        self.lenght = 0
        self.score = 0
        self.timeStamp = -1
        self.currentQuestion = -1

        self.wrong = []
        self.skipped = []

    def prepare(self, _number, _customQuestions = None):
        dataManager = DataManager()

        _jsonQuiz = dataManager.load("quiz")
        if not _jsonQuiz:
            return False
        
        if _number <= 0: # if invalid clip it to 1
            _number = 1

        _number = min(_number, util.MAX_QUIZ_LENGHT, len(_jsonQuiz))

        if not _customQuestions: # normal load

            categories = list(set(jsonQuestion["categoria"] for jsonQuestion in _jsonQuiz))
            minCategories = min(_number // 2, len(categories), 15)
            selectedCategories = random.sample(categories, minCategories)

            selectedIDs = [] # useful for getting the remaninig questions later

            for cat in selectedCategories:
                questionInCat = [q for q in _jsonQuiz if q["categoria"] == cat]
                jsonSelectedQuestion = random.choice(questionInCat)

                self.questions.append(Question(
                        jsonSelectedQuestion["id"], 
                        jsonSelectedQuestion["domanda"],
                        jsonSelectedQuestion["risposte"],
                        jsonSelectedQuestion["corretta"],
                        jsonSelectedQuestion["categoria"]
                    ))
                
                selectedIDs.append(jsonSelectedQuestion["id"])
            
            remainingNeeded = _number - len(self.questions)

            if remainingNeeded > 0:
                randomSelectedQuestions = []
                remainingPool = [q for q in _jsonQuiz if q["id"] not in selectedIDs]

                randomSelectedQuestions += random.sample(remainingPool, remainingNeeded)

                for randJsonQ in randomSelectedQuestions:
                    self.questions.append(Question(
                        randJsonQ["id"], 
                        randJsonQ["domanda"],
                        randJsonQ["risposte"],
                        randJsonQ["corretta"],
                        randJsonQ["categoria"]
                    ))
        else:
            # load custom
            for randJsonQ in _customQuestions:
                    self.questions.append(Question(
                        randJsonQ["id"], 
                        randJsonQ["domanda"],
                        randJsonQ["risposte"],
                        randJsonQ["corretta"],
                        randJsonQ["categoria"]
                    ))


        return True
    
    def start(self):

        # Is not a loaded Quiz
        # or an empty one
        if self.startTime == -1 and len(self.questions) > 0: 

            self.startTime = time.time()
            self.currentQuestion = 0
    
    def next(self):
        
        if self.currentQuestion >= 0:
            self.currentQuestion += 1
            if self.currentQuestion == len(self.questions):
                self.currentQuestion = 0

        return self.currentQuestion
    
    def precedent(self):
        
        if self.currentQuestion >= 0:
            self.currentQuestion -= 1
            if self.currentQuestion == -1:
                self.currentQuestion = len(self.questions) - 1
                
        return self.currentQuestion
    
    def answerCurrent(self, _answerValue):
        return self.questions[self.currentQuestion].answer(_answerValue)

    def getCurrent(self):

        if self.currentQuestion >= 0:
            i = self.currentQuestion
            return self.questions[i].category, self.questions[i].question, self.questions[i].answers, self.questions[i].selected

    def getCurrentCorrect(self):

        return self.questions[self.currentQuestion].correct

    def stop(self):

        self.endTime = time.time()
        self.timeStamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for question in self.questions:

            _valuation, _score = question.evaluate()

            if _valuation == util.INCORRECT_ANSWER:
                self.wrong.append(question.id)
            elif _valuation == util.UNASWERED_ANSWER:
                self.skipped.append(question.id)
            
            self.score += _score
        
        return self.score
    
    def save(self):

        if self.endTime <= self.startTime:
            raise Exception("Trying to save an quiz that is not ended")

        result = {
            "timestamp": self.timeStamp,
            "punteggio": f"{self.score:.2f}/{self.getMaxScore()}",
            "sbagliate": self.wrong,
            "skippate": self.skipped
        }

        duration = int(self.endTime - self.startTime)
        total = len(self.questions)
        correct = total - len(self.wrong) - len(self.skipped)
        accuracy = (correct / total) * 100 if total else 0
        categories = sorted(set(q.category for q in self.questions))

        progress_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_questions": total,
            "score": round(self.score, 2),
            "correct": correct,
            "wrong": len(self.wrong),
            "skipped": len(self.skipped),
            "accuracy_percent": round(accuracy, 2),
            "duration_sec": duration,
            "categories": categories
        }

        dataManager = DataManager()
        dataManager.saveTxt("results", result)
        dataManager.saveJson("progress", progress_entry)
        
        
    def getMaxScore(self):
        return len(self.questions) * Question.CORRECT_SCORE
        #implement save

            




