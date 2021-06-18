from django import forms
from .models import ExamCorrect, Neticeler, Imtahan


class ExamCorrectForms(forms.ModelForm):
    class Meta:
        model = ExamCorrect
        fields = ['file', 'descriptions', 'imtahan_id']


class NeticelerForms(forms.ModelForm):
    class Meta:
        model = Neticeler
        fields = ['file', 'descriptions', 'imtahan_id']


class ImtahanForm(forms.ModelForm):
    class Meta:
        model = Imtahan
        fields = ['name', 'tarix']
