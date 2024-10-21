# quizzerapp/models/question.py


from django.db import models
from django.core.exceptions import ValidationError
from .questiontype import QuestionType

class Question(models.Model):
    question_type = models.ForeignKey('QuestionType', on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    
     
    choices = models.JSONField(blank=True, null=True) # For MCQ ,SCQ
    correct_answer = models.CharField(max_length=10, blank=True, null=True) # For TF, MCQ ,SCQ
    
    # For Match the Following ,
    match_the_following = models.JSONField(blank=True, null=True)
    correct_answer_pairs = models.JSONField(blank=True, null=True)

    #for fill in the blanks
    blanks = models.JSONField(blank=True, null=True)  


    def clean(self):
        # Validation for MCQ type questions
        if self.question_type.question_type_code == 'SCQ':
            if not self.choices or len(self.choices) != 4:
                raise ValidationError("Minimum Four choices are required for SCQ.")
            if not self.correct_answer or self.correct_answer not in self.choices.values():
                raise ValidationError("Correct answer must be one of the provided choices.")

        # Validation for Match the Following type questions
        if self.question_type.question_type_code == 'MTF':
            if not self.match_the_following:
                raise ValidationError("Match the Following pairs are required.")
            if not self.correct_answer_pairs:
                raise ValidationError("Correct answer pairs are required.")

            # Ensure the keys are the same in both match_the_following and correct_answer_pairs
            if set(self.match_the_following.keys()) != set(self.correct_answer_pairs.keys()):
                raise ValidationError("Keys for match pairs and correct answers must be the same.")

        # Validation for Fill in the Blanks type questions
        if self.question_type.question_type_code == 'FIB':
            if not self.blanks or not isinstance(self.blanks, list):
                raise ValidationError("Blanks must be a list and cannot be empty.")
            
            for blank in self.blanks:
                if 'blank_number' not in blank or 'correct_answer' not in blank:
                    raise ValidationError("Each blank must have a 'blank_number' and 'correct_answer'.")
            
            # Validate that the number of answers provided matches the number of blanks
            if len(self.blanks) != len([b for b in self.blanks if 'correct_answer' in b]):
                raise ValidationError("The number of answers provided must match the number of blanks.")
