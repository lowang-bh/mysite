from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.http import HttpResponse
from .models import Question
# Create your views here.


def index(request):
    try:
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
    except Question.DoesNotExist:
        raise Http404("Question doesn't exist.")
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def index1(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def index2(request):
    output = "Hello, world. You're at the polls index."
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output += ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
