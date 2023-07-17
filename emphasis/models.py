from django.db import models
from django.contrib.auth.models import User


class Words(models.Model):
    words_without_emphasis = models.CharField(max_length=100)
    words_emphasis = models.CharField(max_length=100)

    def __str__(self):
        return self.words_emphasis


class Mistakes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word_mistakes = models.CharField(max_length=100)
    word_mistakes_counter = models.IntegerField(default=0)


class Statistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    all_mistakes = models.IntegerField(default=0)
    all_right = models.IntegerField(default=0)
