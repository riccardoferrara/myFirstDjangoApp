from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You are looking at the question %s" % question_id)

def results(request, question_id):
    reponse = "your are looking at the results of question %s"
    return HttpResponse(reponse % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting the question %s" % question_id)
