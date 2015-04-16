"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime

from .models import Question

def home(request):
    """Renders home page."""
    #assert isinstance(RequestContext, HttpRequest)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question_text for p in latest_question_list])
    return render(
        request,
        'polls/index.html',
        context_instance = RequestContext(request,
        {
            'title': 'Polls Home',
            'year':datetime.now().year,
            'latest_question_list': output,
        })
    )

def detail(request, question_id):
    return HttpResponse("You're looking at question {0}.".format(question_id))

def results(request, question_id):
    response = "You're looking at the results of question {0}."
    return HttpResponse(response.format(question_id))

def vote(request, question_id):
    return HttpResponse("You're voting on question {0}.".format(question_id))