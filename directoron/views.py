from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from directoron.models import Question


# Create your views here.
def index(request):
    # query 5 date order by descending from database
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("directoron/index.html")
    context = {"latest_question_list": latest_question_list}

    # manually and comprehensive method
    # return HttpResponse(template.render(context, request))

    # shortcut method
    return render(request, "directoron/index.html", context)


def vote(request, question_id):
    return HttpResponse("You're voting on question {}".format(question_id))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return HttpResponse("You are looking at question {}.".format(question_id))