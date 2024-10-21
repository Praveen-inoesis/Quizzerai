# # # quizzerapp/utils/questions.py


# from django.core.exceptions import ObjectDoesNotExist
# from ..models import QuestionType

# def validate_question_data(data):
#     """
#     Validates the incoming data for creating/updating a question.
#     This is a utility function for validating based on question type.
#     """
#     question_type_id = data.get('question_type')

#     # Validate the question type ID
#     try:
#         question_type = QuestionType.objects.get(id=question_type_id)
#     except ObjectDoesNotExist:
#         return False, {"error": "Invalid question type ID."}

#     # Validation for Match the Following (MTF)
#     if question_type.question_type_code == 'MTF':
#         if 'match_the_following' not in data or 'correct_answer_pairs' not in data:
#             return False, {"error": "For MTF, 'match_the_following' and 'correct_answer_pairs' are required."}

#     # Validation for Single Choice Questions (SCQ)
#     elif question_type.question_type_code == 'SCQ':
#         if 'choices' not in data or 'correct_answer' not in data:
#             return False, {"error": "For SCQ, 'choices' and 'correct_answer' are required."}
#         if data.get('correct_answer') not in data['choices'].values():
#             return False, {"error": "The correct answer must be one of the provided choices."}

#     # Validation for Multiple Choice Questions (MCQ)
#     elif question_type.question_type_code == 'MCQ':
#         if 'choices' not in data or 'correct_answer' not in data:
#             return False, {"error": "For MCQ, 'choices' and 'correct_answer' are required."}
        
#         # Check if the correct answer consists of more than one option
#         correct_answers = [ans.strip() for ans in data['correct_answer'].split(',')]
        
#         if len(correct_answers) < 1:
#             return False, {"error": "For MCQ, there must be at least one correct answer."}

#         # Check if all correct answers are among the provided choices
#         for answer in correct_answers:
#             if answer not in data['choices'].values():
#                 return False, {"error": f"The answer '{answer}' is not among the provided choices."}
        
#         # Optionally, validate the count of correct answers
#         if len(correct_answers) > len(data['choices']):
#             return False, {"error": "The number of correct answers cannot exceed the number of choices."}

#     # Validation for True/False Questions (TF)
#     elif question_type.question_type_code == 'TF':
#         if data.get('correct_answer') not in ["True", "False"]:
#             return False, {"error": "Correct answer must be 'True' or 'False'."}

#     return True, {}

#quizzerapp/utils/questions.py

# quizzerapp/utils/questions.py

import re
from django.core.exceptions import ObjectDoesNotExist
from ..models import QuestionType

def validate_question_data(data):
    """
    Validates the incoming data for creating/updating a question.
    This utility function validates based on question type.
    """
    question_type_id = data.get('question_type')

    # Validate the question type ID
    try:
        question_type = QuestionType.objects.get(id=question_type_id)
    except ObjectDoesNotExist:
        return False, {"error": "Invalid question type ID."}

    # Validation for Match the Following (MTF)
    if question_type.question_type_code == 'MTF':
        if 'match_the_following' not in data or 'correct_answer_pairs' not in data:
            return False, {"error": "For MTF, 'match_the_following' and 'correct_answer_pairs' are required."}

    # Validation for Single Choice Questions (SCQ)
    elif question_type.question_type_code == 'SCQ':
        if 'choices' not in data or 'correct_answer' not in data:
            return False, {"error": "For SCQ, 'choices' and 'correct_answer' are required."}
        if data.get('correct_answer') not in data['choices'].values():
            return False, {"error": "The correct answer must be one of the provided choices."}

    # Validation for Multiple Choice Questions (MCQ)
    elif question_type.question_type_code == 'MCQ':
        if 'choices' not in data or 'correct_answer' not in data:
            return False, {"error": "For MCQ, 'choices' and 'correct_answer' are required."}

        # Check if the correct answer consists of more than one option
        correct_answers = [ans.strip() for ans in data['correct_answer'].split(',')]

        if len(correct_answers) < 1:
            return False, {"error": "For MCQ, there must be at least one correct answer."}

        # Check if all correct answers are among the provided choices
        for answer in correct_answers:
            if answer not in data['choices'].values():
                return False, {"error": f"The answer '{answer}' is not among the provided choices."}

        # Optionally, validate the count of correct answers
        if len(correct_answers) > len(data['choices']):
            return False, {"error": "The number of correct answers cannot exceed the number of choices."}

    # Validation for True/False Questions (TF)
    elif question_type.question_type_code == 'TF':
        if data.get('correct_answer') not in ["True", "False"]:
            return False, {"error": "Correct answer must be 'True' or 'False'."}

    # Validation for Fill in the Blanks (FIB)
    elif question_type.question_type_code == 'FTB':
        if 'question_text' not in data or 'blanks' not in data or not isinstance(data['blanks'], list):
            return False, {"error": "For FTB, 'question_text' and 'blanks' are required, and 'blanks' must be a list."}

        # Count the number of blank placeholders (_______) in the question_text
        number_of_blanks_in_text = len(re.findall(r'_{3,}', data['question_text']))  # Matches any occurrence of 3 or more underscores

        # Validate that the number of provided blanks (answers) matches the number of blanks in the text
        provided_blanks = len(data['blanks'])

        if number_of_blanks_in_text != provided_blanks:
            return False, {
                "error": f"The number of blanks in the question text ({number_of_blanks_in_text}) does not match the number of provided answers ({provided_blanks})."
            }

        # Validate that each blank has a correct answer and a blank number
        for blank in data['blanks']:
            if 'correct_answer' not in blank or 'blank_number' not in blank:
                return False, {"error": "Each blank must have a 'correct_answer' and 'blank_number'."}

    # If none of the question types matched, return a default False, indicating failure
    else:
        return False, {"error": "Unknown question type."}

    # Return True if everything is valid
    return True, {}


