#quizzerapp\utils\questionbank.py

from rest_framework.exceptions import ValidationError
from quizzerapp.models.questions import Question

def validate_question_bank_name(name):
    if not name or len(name.strip()) == 0:
        raise ValidationError("Question Bank name cannot be empty.")
    if len(name) > 255:
        raise ValidationError("Question Bank name cannot exceed 255 characters.")

def validate_question(question_id):
    try:
        Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise ValidationError(f"Question with ID {question_id} does not exist.")

def validate_questions(questions):
    if not isinstance(questions, list):
        raise ValidationError("Questions must be a list of question IDs.")
    
    for question_id in questions:
        validate_question(question_id)
