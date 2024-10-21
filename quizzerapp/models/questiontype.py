# quizzerapp/models/questiontype.py

from django.db import models

class QuestionType(models.Model):
    title = models.CharField(max_length=255)
    question_type_code = models.CharField(max_length=10, unique=True)  # Ensure this exists
    description = models.TextField()

    def __str__(self):
        return self.title

