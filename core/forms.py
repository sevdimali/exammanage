from django import forms
from .models import ExamCorrect

class ExamCorrectForms(forms.ModelForm):
    class Meta:
        model=ExamCorrect
        fields=['file','descriptions','imtahan_id']

