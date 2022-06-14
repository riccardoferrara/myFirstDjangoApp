from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    # load the template
    template = loader.get_template('polls/index.html')
    # create variable to pass to the template
    context = {'latest_question_list': latest_question_list}
    # give response rendering the template
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You are looking at the question %s" % question_id)

def results(request, question_id):
    reponse = "your are looking at the results of question %s"
    return HttpResponse(reponse % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting the question %s" % question_id)
