from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404


from .models import Question, Answer

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def void(request):
	raise Http404

def new(request):
	questions = Question.objects.all().order_by('-id')
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
	questions = Question.objects.all().order_by('-rating')
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
	return render(request, 'qa/question.html', {
		'question' : question,
		'answers' : Answer.objects.filter(question=question),
	})