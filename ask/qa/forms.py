from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField()
    
    def clean(self):
        pass

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.ModelChoiceField(queryset=Question.objects.all())

    def clean(self):
        pass

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = 1
        answer.save()
        return answer