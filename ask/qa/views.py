from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import AskForm, AnswerForm, SignUpForm, LoginForm
import datetime
from django.utils import timezone



from .models import Question, Answer, User, do_login

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def void(request):
	raise Http404

def new(request):
	questions = Question.objects.new()
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/?page='
	page = paginator.page(page)
	for q in page.object_list:
		print(q.text)
	return render(request, 'qa/new.html', {
		'questions': page.object_list,
		'paginator': paginator,
		'page' : page,
	})

def popular(request):
	questions = Question.objects.popular()
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/?page='
	page = paginator.page(page)
	for q in page.object_list:
		print(q.text)
	return render(request, 'qa/popular.html', {
		'questions': page.object_list,
		'paginator': paginator,
		'page' : page,
	})


def question(request, id):

	try:
		question = Question.objects.get(id=id)
	except Question.DoesNotExist:
		raise Http404

	if request.method == "POST":
		form = AnswerForm(request.POST)
		user = request.user
		if form.is_valid():
			answer = form.save()
			answer.user = user
			answer = form.save()
			url = answer.question.get_url()
			return HttpResponseRedirect(url)
	else:
		form = AnswerForm()
		
	return render(request, 'qa/question.html', {
		'question' : question,
		'answers' : Answer.objects.filter(question=question),
		'form' : form
	})

def ask(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		user = request.user
		if form.is_valid():
			question = form.save()
			question.user = user
			question = form.save()
			url = question.get_url()
			return HttpResponseRedirect(url)
	else:
		form = AskForm()
	return render(request, 'qa/ask.html', {
		'form' : form
	})

def signup(request):
	error = ''
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			url = request.POST.get('/')
			sessionid = do_login(user.username, user.password)
			response = HttpResponseRedirect(url)
			response.set_cookie('sessionid', sessionid,
				domain='localhost', httponly=True,
				expires=timezone.now() + datetime.timedelta(days=5)
			)
			return response
		else:
			error = u'Wrong format of data'
	form = SignUpForm()
	return render(request, 'qa/signup.html',{
		'error' : error,
		'form' : form,
	})




def login(request):
	error = ''
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password  = form.cleaned_data['password']
			url = '/'
			sessionid = do_login(username, password)
			if sessionid:
				response = HttpResponseRedirect(url)
				response.set_cookie('sessionid', sessionid,
					domain='localhost', httponly=True,
					expires=timezone.now() + datetime.timedelta(days=5)
				)
				return response
			else:
				error = u'Wrong username / password'
		else:
			error = u'Wrong format of data'
	form = LoginForm()
	return render(request, 'qa/login.html', {
		'error' : error,
		'form' : form,
	})