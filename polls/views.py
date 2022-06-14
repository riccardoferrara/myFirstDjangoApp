from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpRequest


from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    # give response rendering the template
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    reponse = "your are looking at the results of question %s"
    return HttpResponse(reponse % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting the question %s" % question_id)
