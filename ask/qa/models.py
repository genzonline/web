import datetime
import random
from django.utils import timezone
from django.db import models

class QuestionManager(models.Manager):
	def new(self):
	    return self.order_by('-added_at')

	def popular(self):
	    return self.order_by('-rating')

class User(models.Model):
	login = models.CharField(max_length=100, unique=True)
	email = models.EmailField()
	password = models.CharField(max_length=100)

class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(max_length=100)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	likes = models.ManyToManyField(User, related_name='question_like_user')

	def __unicode__(self):
		return self.text

	def get_url(self):
		return '/question/%d/' % self.id


class Answer(models.Model):
	text = models.CharField(max_length=255)
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Session(models.Model):
	key = models.CharField(max_length=100, unique=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	expires = models.DateTimeField()

def do_login(login, password):
	try:
		user = User.objects.get(login=login)
	except User.DoesNotExist:
		return None
	hashed_pass = salt_and_hash(password)
	if user.password != hashed_pass:
		return None
	session = Session(
		key = generate_long_random_key(login),
		user = user,
		expires = timezone.now() + datetime.timedelta(days=5),
	)
	session.save()       # <<----------------------- ТУТ ПРОГА ФАКАПАЕТСЯ
	return session.key

def salt_and_hash(password):
	return password

def generate_long_random_key(login):
	return '{}'.format(login) + str(random.randrange(1, 2**63 - 1))