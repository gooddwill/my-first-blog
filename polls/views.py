from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
# Create your views here.



def index(request) :
#	return HttpResponse("Hello, world You're at the polls index.")
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
	template = loader.get_template('polls/index.html')
 #   return HttpResponse(output)
	context = {
		'latest_question_list' : latest_question_list,
		}
	return HttpResponse(template.render(context, request))
	
def detail(request, question_id) :
	try :
		question = Question.object.get(pk=question_id)
	except Question.DoesNotExist :
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html',{'question':question})
#	return HttpResponse("You're looking at question %s." % question_id)
	
def results(request, question_id) :
	response = "You're looking at the resutls of question %s."
	return HttpResponse(response % question_id)
	
def vote(request, question_id) :
	return HttpResponse("You're voting on question %s." % question_id)