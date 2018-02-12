from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Question, Choice
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
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does't exsit")
    return render(request, 'polls/detail.html', {'question':question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
    #return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question,
                                                     'error_message':"You didn't select a choice",})
    else:
        selected_choice.votes +=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
