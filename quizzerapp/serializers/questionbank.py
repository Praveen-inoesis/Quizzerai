# # quizzerapp/serializers/questionbank.py

# from rest_framework import serializers
# from quizzerapp.models.questionbank import QuestionBank
# from quizzerapp.models.questions import Question
# from .questiontype import QuestionTypeSerializer

# class QuestionBankQuestionSerializer(serializers.ModelSerializer):
#     question_type = QuestionTypeSerializer()

#     class Meta:
#         model = Question
#         fields = [
#             'id', 
#             'question_type', 
#             'question_text', 
#             'choices', 
#             'correct_answer', 
#             'match_the_following', 
#             'correct_answer_pairs',
#             'blanks'  
#         ]

# class QuestionTypeGroupSerializer(serializers.Serializer):
#     question_type = serializers.IntegerField(source='question_type.id')
#     name = serializers.CharField(source='question_type.title')
#     questions = QuestionBankQuestionSerializer(many=True)

# class QuestionBankSerializer(serializers.ModelSerializer):
#     questions = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), many=True, required=False)

#     class Meta:
#         model = QuestionBank
#         fields = ['id', 'name', 'description', 'questions']

#     def to_representation(self, instance):
#         """
#         Customize the representation to group questions by their type
#         and include the blanks field for FIB questions.
#         """
#         representation = {
#             'question_banks_id': instance.id,
#             'name': instance.name,  # Keep name as it is
#             'description': instance.description,  # Keep description as it is
#             'question_type': []
#         }

#         # Group questions by their type
#         grouped_questions = {}
#         for question in instance.questions.all():
#             question_type_id = question.question_type.id if question.question_type else None
#             if question_type_id not in grouped_questions:
#                 grouped_questions[question_type_id] = {
#                     'question_type': question_type_id,
#                     'name': question.question_type.title if question.question_type else None,
#                     'questions': []
#                 }

#             # Create a question representation
#             question_representation = {
#                 'question_id': question.id,
#                 'question_text': question.question_text,
#             }

#             # Only add fields that are not None
#             if question.choices is not None:
#                 question_representation['choices'] = question.choices
#             if question.correct_answer is not None:
#                 question_representation['correct_answer'] = question.correct_answer
#             if question.match_the_following is not None:
#                 question_representation['match_the_following'] = question.match_the_following
#             if question.correct_answer_pairs is not None:
#                 question_representation['correct_answer_pairs'] = question.correct_answer_pairs

#             # Include blanks if the question type is "Fill in the Blanks"
#             if question.question_type.question_type_code == 'FIB':
#                 question_representation['blanks'] = question.blanks

#             # Add the question representation to the group
#             grouped_questions[question_type_id]['questions'].append(question_representation)

#         # Filter out any groups that have null values for 'name' or 'question_type'
#         for group in grouped_questions.values():
#             if group['name'] is not None and group['question_type'] is not None:
#                 representation['question_type'].append(group)

#         # Remove name and description from representation if they are None
#         if representation['name'] is None:
#             del representation['name']
#         if representation['description'] is None:
#             del representation['description']

#         return representation

# quizzerapp/serializers/questionbank.py

from rest_framework import serializers
from quizzerapp.models.questionbank import QuestionBank
from quizzerapp.models.questions import Question
from .questiontype import QuestionTypeSerializer

class BlankSerializer(serializers.Serializer):
    blank_number = serializers.IntegerField()
    correct_answer = serializers.CharField()

class QuestionBankQuestionSerializer(serializers.ModelSerializer):
    question_type = QuestionTypeSerializer()
    blanks = BlankSerializer(many=True, required=False)  # Add blanks serializer

    class Meta:
        model = Question
        fields = [
            'id', 
            'question_type', 
            'question_text', 
            'choices', 
            'correct_answer', 
            'match_the_following', 
            'correct_answer_pairs', 
            'blanks'  # Include blanks field for FTB questions
        ]

class QuestionTypeGroupSerializer(serializers.Serializer):
    question_type = serializers.IntegerField(source='question_type.id')
    name = serializers.CharField(source='question_type.title')
    questions = QuestionBankQuestionSerializer(many=True)

class QuestionBankSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), many=True, required=False)

    class Meta:
        model = QuestionBank
        fields = ['id', 'name', 'description', 'questions']

    def to_representation(self, instance):
        """
        Customize the representation to group questions by their type
        and include the blanks field for Fill in the Blanks (FTB) questions.
        """
        representation = {
            'question_banks_id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'question_type': []
        }

        grouped_questions = {}
        for question in instance.questions.all():
            question_type_id = question.question_type.id if question.question_type else None
            if question_type_id not in grouped_questions:
                grouped_questions[question_type_id] = {
                    'question_type': question_type_id,
                    'name': question.question_type.title if question.question_type else None,
                    'questions': []
                }

            # Create a question representation
            question_representation = {
                'question_id': question.id,
                'question_text': question.question_text,
            }

            # Add fields only if they exist
            if question.choices is not None:
                question_representation['choices'] = question.choices
            if question.correct_answer is not None:
                question_representation['correct_answer'] = question.correct_answer
            if question.match_the_following is not None:
                question_representation['match_the_following'] = question.match_the_following
            if question.correct_answer_pairs is not None:
                question_representation['correct_answer_pairs'] = question.correct_answer_pairs

            # Check if the question type is "Fill in the Blanks" (FTB) and include blanks
            if question.question_type and question.question_type.question_type_code == 'FTB' and question.blanks:
                blanks_data = [
                    {
                        'blank_number': i + 1,
                        'correct_answer': blank['correct_answer']
                    }
                    for i, blank in enumerate(question.blanks)
                ]
                question_representation['blanks'] = blanks_data

            # Add the question to its respective group
            grouped_questions[question_type_id]['questions'].append(question_representation)

        # Filter out groups with missing 'name' or 'question_type'
        for group in grouped_questions.values():
            if group['name'] is not None and group['question_type'] is not None:
                representation['question_type'].append(group)

        return representation


