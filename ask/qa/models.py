from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)# - заголовок вопроса
    text = models.TextField()# - полный текст вопроса
    added_at = models.DateTimeField()# - дата добавления вопроса
    rating = models.IntegerField()# - рейтинг вопроса (число)
    #author = models.# - автор вопроса
    #likes = models.# - список пользователей, поставивших "лайк"

class Answer(models.Model): #  - ответ
    text = models.TextField()# - текст ответа
    added_at = models.DateTimeField()# - дата добавления ответа
    question = models.# - вопрос, к которому относится ответ
    author = models.# - автор ответа