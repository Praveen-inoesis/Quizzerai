# # quizzerapp/forms.py


from django import forms
from .models.questions import Question

class QuestionAdminForm(forms.ModelForm):
    # Fields for Multiple Choice Questions
    choice_1 = forms.CharField(max_length=200, required=False)
    choice_2 = forms.CharField(max_length=200, required=False)
    choice_3 = forms.CharField(max_length=200, required=False)
    choice_4 = forms.CharField(max_length=200, required=False)

    # Fields for Match the Following Questions
    mtf_item_pairs = forms.CharField(widget=forms.Textarea, help_text="Enter pairs as 'Key: Value' (one pair per line)")

    class Meta:
        model = Question
        fields = '__all__'

    def save(self, commit=True):
        question = super().save(commit=False)

        # Set choices for MCQ
        if self.cleaned_data['question_type'].question_type_code == 'MCQ':
            question.choices = {
                'choice_1': self.cleaned_data['choice_1'],
                'choice_2': self.cleaned_data['choice_2'],
                'choice_3': self.cleaned_data['choice_3'],
                'choice_4': self.cleaned_data['choice_4'],
            }

        # Process match the following pairs
        elif self.cleaned_data['question_type'].question_type_code == 'MTF':
            pairs = self.cleaned_data['mtf_item_pairs'].strip().split('\n')
            match_dict = {}
            for pair in pairs:
                if ':' in pair:
                    key, value = pair.split(':', 1)
                    match_dict[key.strip()] = value.strip()
                else:
                    raise forms.ValidationError(f"Invalid format for pair: {pair}")

            question.match_the_following = match_dict

        if commit:
            question.save()
        return question

