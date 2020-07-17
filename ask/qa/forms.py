from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):
		pass

	def save(self):
		u = User.objects.get(id=1)
		question = Question(**self.cleaned_data, author=u)
		question.save()
		return question

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)

	choices = []
	for i in Question.objects.all()[:]:
		choices.append(("{}".format(i.id), "{}".format(i.id)))


	question = forms.ChoiceField(choices=choices)

	def clean(self):
		pass

	def save(self):
		u = User.objects.get(id=1)
		answer = Answer(text=self.cleaned_data['text'], question_id=int(self.cleaned_data['question']), author=u)
		answer.save()
		return answer