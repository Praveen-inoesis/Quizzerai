 # quizzerapp/views/questiontype.py


from rest_framework import viewsets
from ..models.questiontype import QuestionType
from ..serializers.questiontype import QuestionTypeSerializer

class QuestionTypeViewSet(viewsets.ModelViewSet):
    queryset = QuestionType.objects.all()
    serializer_class = QuestionTypeSerializer
