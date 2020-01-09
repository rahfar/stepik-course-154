from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField()

    def save(self):
        question = Question(author = self._user, **self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.ModelChoiceField(queryset=Question.objects.all())

    def save(self):
        answer = Answer(author = self._user, **self.cleaned_data)
        answer.save()
        return answer


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user