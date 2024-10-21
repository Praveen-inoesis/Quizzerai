# quizzerapp/models/questiontype.py

from rest_framework import serializers
from ..models.questiontype import QuestionType

class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = '__all__'
