# quizzerapp/serializers/question.py

#new code
# from rest_framework import serializers
# from ..models.questions import Question

# class QuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = '__all__'

#     def validate(self, data):
#         """
#         Ensure the data is valid before creating/updating the question.
#         """
#         question_type = data.get('question_type')
#         if question_type:
#             question = Question(**data)
#             question.clean()  # Call the model's clean method for validation
#         return data

#     def to_representation(self, instance):
#         """
#         Customize response to remove unnecessary fields based on the question type
#         and filter out null values.
#         """
#         representation = super().to_representation(instance)

#         # Remove fields based on question type
#         if instance.question_type.question_type_code == 'MCQ':
#             representation.pop('match_the_following', None)
#             representation.pop('correct_answer_pairs', None)
#         elif instance.question_type.question_type_code == 'MTF':
#             representation.pop('choices', None)
#             representation.pop('correct_answer', None)

#         # Filter out fields that have null values
#         representation = {key: value for key, value in representation.items() if value is not None}

#         return representation

#quizzerapp/serializers/questions.py

from rest_framework import serializers
from ..models.questions import Question

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = '__all__'
    
    def to_representation(self, instance):
        # Get the original representation (which includes all fields)
        representation = super().to_representation(instance)
        
        # Remove any fields that have a value of `None` (null in JSON)
        return {key: value for key, value in representation.items() if value is not None}
