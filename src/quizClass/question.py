import src.quizClass.utility as util

class Question(object):

    CORRECT_SCORE = util.ADD_CORRECT_SCORE
    INCORRECT_SCORE = util.ADD_INCORRECT_SCORE
    UNASWERED_SCORE = util.ADD_UNANSWERED_SCORE

    def __init__(self, _id, _question, _answers, _correct, _category):

        self.id = _id
        self.question = _question
        self.answers = _answers
        self.correct = _correct
        self.category = _category
        self.selected = -1
    
    def answer(self, _answerId):

        if _answerId >= len(self.answers):

            return False # Invalid answer
        
        elif _answerId < 0:

            self.selected = -1 # Deselect the answer
            return True
        
        else:

            self.selected = _answerId # Select an avaible answer
            return True

    def evaluate(self):

        if self.selected == -1:

            return util.UNASWERED_ANSWER, self.UNASWERED_SCORE 
        
        elif self.selected == self.correct:

            return util.CORRECT_ANSWER, self.CORRECT_SCORE 
        
        else:

            return util.INCORRECT_ANSWER, self.INCORRECT_SCORE 
    


