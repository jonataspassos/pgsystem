from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import User

# Create your models here.


class Tournament(models.Model):
    name = models.CharField(_('Name'),max_length=30)
    thema = models.CharField(_('Thema'),max_length=30,default="")
    create = models.DateField(auto_now=True)
    end = models.DateField(_('End'),blank=True, null=True)
    def __str__(self):
        return ((self.thema +': ')if self.thema else '') + self.name


class Test(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.SET_NULL, blank=True, null=True)
    code = models.CharField(max_length=30)
    desc = models.TextField(_("Description"),blank=True, null=True)
    create = models.DateField(_('Creation'),auto_now=True)
    aplicate = models.DateField(_('Aplication'), blank=True, null=True)
    def __str__(self):
        return ((str(self.tournament)+': ')if self.tournament else '') + self.code

#Proposição Genérica
"""Serve para representar respostas e alternativas"""
class Proposition(models.Model):
    PROPOSITION_TYPES = [
        ('INT','Integer Number'),
        ('TXT','Text'),
        ('FLT','Float Number'),
        ('BOL','Boolean'),
        ('GRP','Group')
    ]
    PROPOSITION_TYPE = models.CharField(max_length=3,default="GEN", choices = PROPOSITION_TYPES)
    proposition_field = None
    desc = models.CharField(_("Description"),blank=True, null=True,max_length=30)
    create = models.DateField(auto_now=True)
    value = models.PositiveIntegerField(_('Value'),default=1)
    def __str__(self):
        return self.PROPOSITION_TYPE + ((" - "+str(self.proposition_field))if self.proposition_field else ((" - "+ self.desc)if self.desc else ''))

#Questão genérica
"""Serve para definir a questão"""
class Question(models.Model):
    QUESTION_TYPES=[
        ('CHO','Multiple Choice'),
        ('TOF','True or False'),
        ('OPN','Open'),
        ('SUM','Summation'),
        ('PRO','Multiple Propositions'),
        ('GRP','Group'  )
    ]
    QUESTION_TYPE = models.CharField(max_length=3,default="GEN",choices = QUESTION_TYPES)
    test = models.ManyToManyField(Test,related_name="from_test") #A qual teste Pertence
    statement = models.TextField(default="")#enunciado da questão
    value = models.FloatField(_('Value'),default=1.0)#valor da questão
    def __str__(self):
        return self.QUESTION_TYPE +" - "+ str(self.statement)[:20]

#Para registrar respostas
class UserResponse(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    test = models.ForeignKey(Test,on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    response = models.ForeignKey(Proposition,on_delete=models.CASCADE, blank=True, null=True)
    score = models.FloatField(_("Score"),default=0)
    def __str__(self):
        return ((str(self.test)+': ')if self.test else '') + str(self.question)[:20]+('...'if len(str(self.question))>20 else '') +" - "+ str(self.user) + (' - Respondido' if self.response else '')

#Proposições Específicas
"""
Quando for necessário criar uma proposição específica, 
adicione seu model abaixo, adicione uma opção para ela no 
    PROPOSITION_TYPES da classe genérica e no 
    PROPOSITION_TYPES deste arquivo, ao final das 
        classes das proposições específicas
"""

"""Para quando a proposição for um numero inteiro"""
class IntegerProposition(Proposition):
    PROPOSITION_TYPE = 'INT'
    proposition_field = models.PositiveIntegerField(_("Number"),default=0)

"""Para quando a proposição for um Texto"""
class TextProposition(Proposition):
    PROPOSITION_TYPE = 'TXT'
    proposition_field = models.TextField(_("Text"),default="")

"""Para quando a proposição for um numero Flutuante"""
class FloatProposition(Proposition):
    PROPOSITION_TYPE = 'FLT'
    proposition_field = models.FloatField(_("Number"),default=0.0)

"""Para quando a proposição for verdadeiro ou falso"""
class BooleanProposition(Proposition):
    PROPOSITION_TYPE = 'BOL'
    proposition_field = models.NullBooleanField(_("Yes or No"), blank=True, null=True)

"""Para quando a proposição for um conjunto de proposições"""
class GroupProposition(Proposition):
    PROPOSITION_TYPE = 'GRP'
    proposition_field = models.ManyToManyField(Proposition,related_name='group_propositions')

PROPOSITION_TYPES = [
        ('INT',IntegerProposition),
        ('TXT',TextProposition),
        ('FLT',FloatProposition),
        ('BOL',BooleanProposition),
        ('GRP',GroupProposition)
    ]

#Questões Específicas

"""Questão de Multipla Escolha"""
class MultipleChoiceQuestion(Question):
    QUESTION_TYPE = 'CHO'
    alternative = models.ManyToManyField(Proposition,related_name="multiple_choice_alternative")
    answer = models.ForeignKey(Proposition,on_delete=models.SET_NULL,related_name='multiple_choice_answer', blank=True, null=True)

"""Questão de Verdadeiro ou Falso"""
class TrueOrFalseQuestion(Question):
    QUESTION_TYPE = 'TOF'
    proposition = models.ForeignKey(Proposition,on_delete=models.SET_NULL,related_name='true_or_false_proposition', blank=True, null=True)
    answer = models.ForeignKey(BooleanProposition,on_delete=models.SET_NULL,related_name="true_or_false_answer", blank=True, null=True)

"""Questão Aberta (Exige avaliação)"""
class OpenQuestion(Question):
    QUESTION_TYPE = 'OPN'
    answer = models.ForeignKey(Proposition,on_delete=models.SET_NULL,related_name='open_question_answer', blank=True, null=True)

"""Questão de Soma"""
class SumTypeQuestion(Question):
    QUESTION_TYPE = 'SUM'
    alternative = models.ManyToManyField(Proposition,related_name="sum_type_alternative")
    answer = models.ForeignKey(IntegerProposition,on_delete=models.SET_NULL,related_name="sum_type_answer", blank=True, null=True)

"""Questão de I II III IV V VI ..."""
class ManyPropositionQuestion(Question):
    QUESTION_TYPE = 'PRO'
    proposition = models.ManyToManyField(Proposition,related_name="many_proposition_proposition")
    alternative = models.ManyToManyField(GroupProposition,related_name="many_proposition_alternative")
    answer = models.ForeignKey(GroupProposition,on_delete=models.SET_NULL,related_name='many_proposition_answer', blank=True, null=True)

""" Questão de itens """
class GroupQuestion(Proposition):
    QUESTION_TYPE = 'GRP'
    questions = models.ManyToManyField(Question,related_name='group_questions')

QUESTION_TYPES=[
        ('CHO',MultipleChoiceQuestion),
        ('TOF',TrueOrFalseQuestion),
        ('OPN',OpenQuestion),
        ('SUM',SumTypeQuestion),
        ('PRO',ManyPropositionQuestion),
        ('GRP',GroupQuestion)
    ]