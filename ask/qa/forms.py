from django import forms
from .models import Question, User, salt_and_hash, Answer


class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)

	def clean(self):
		return self.cleaned_data

class SignUpForm(forms.Form):
	username = forms.CharField(max_length=100)
	email = forms.EmailField()
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)

	def clean(self):
		return self.cleaned_data

	def save(self):
		user = User(
			username=self.cleaned_data['username'],
			email=self.cleaned_data['email'],
			password=salt_and_hash(self.cleaned_data['password'],)
		)
		user.save()
		return user

class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(max_length=250, widget=forms.Textarea)

	def clean(self):
		return self.cleaned_data

	def save(self):
		user = User.objects.get(id=1)
		question = Question(text=self.cleaned_data['text'], title=self.cleaned_data['title'], author=user)
		question.save()
		return question

class AnswerForm(forms.Form):
	text = forms.CharField(max_length=250, widget=forms.Textarea)

	choices = []
	for i in Question.objects.all()[:]:
		choices.append(("{}".format(i.id), "{}".format(i.title)))


	question = forms.ChoiceField(choices=choices)

	def clean(self):
		pass

	def save(self):
		user = User.objects.get(id=1)
		answer = Answer(text=self.cleaned_data['text'], question_id=int(self.cleaned_data['question']), author=user)
		answer.save()
		return answer