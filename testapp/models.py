from django.db import models


class Quiz(models.Model):
    question = models.CharField(max_length=500)
    correct = models.CharField(max_length=100)
    wrong = models.CharField(max_length=200)
