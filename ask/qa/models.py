import datetime

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
	def new(self):
	    return self.order_by('-added_at')

	def popular(self):
	    return self.order_by('-rating')

class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(max_length=100)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, related_name='question_like_user')

	def __unicode__(self):
		return self.text


class Answer(models.Model):
	text = models.CharField(max_length=500)
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)


# Create your models here.
