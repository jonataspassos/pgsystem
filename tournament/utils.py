from .models import Question,QUESTION_TYPES
from .models import Proposition,PROPOSITION_TYPES

def convert_question(question):
    for i in QUESTION_TYPES:
        if question.QUESTION_TYPE == i[0]:
            question = i[1].objects.filter(id=question.id)[0]
    return question

def convert_proposition(proposition):
    for i in PROPOSITION_TYPES:
        if proposition.PROPOSITION_TYPE == i[0]:
            proposition = i[1].objects.filter(id=proposition.id)[0]
    return proposition