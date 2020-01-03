from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField()
    
    def clean(self):
        pass

    def save(self):
        pass

class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.CharField()
    def clean(self):
        pass

    def save(self):
        pass