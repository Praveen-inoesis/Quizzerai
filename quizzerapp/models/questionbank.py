# quizzerapp/models/questionbank.py

from django.db import models

class QuestionBank(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    questions = models.ManyToManyField('quizzerapp.Question', related_name='question_banks')

    def __str__(self):
        return self.name


