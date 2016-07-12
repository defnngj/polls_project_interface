from django.shortcuts import get_object_or_404
from .models import Question, Choice
from django.http import HttpResponse
import json


# Create your views here.
# 首页展示所有问题
def questions(request):
    question_list = Question.objects.all()
    datas = {}
    if question_list:
        for question in question_list:
            datas[question.id] = question.question_text
        result = json.dumps({'ststus':200, 'message':'success', 'data':datas})
        return HttpResponse(result)
    else:
        result = json.dumps({'ststus':10022, 'message':'Query result is empty'})
        return HttpResponse(result)


# 查看问题选项
def question_option(request):
    qid = request.GET.get('qid', '')
    if qid == '':
        result = json.dumps({'ststus':10021, 'message': 'Parameter error'})
        return HttpResponse(result)

    choices = Choice.objects.filter(question_id=qid)
    datas = {}

    if choices:
        for choice in choices:
            datas[choice.id] = choice.choice_text
        result = json.dumps({'ststus':200, 'message':'success', 'data':datas})
        return HttpResponse(result)
    else:
        result = json.dumps({'ststus':10022, 'message':'Query result is empty'})
        return HttpResponse(result)


# 查看问题的投票结果
def question_result(request):
    qid = request.GET.get('qid', '')
    if qid == '':
        result = json.dumps({'ststus':10021, 'message':'Parameter error'})
        return HttpResponse(result)

    choices = Choice.objects.filter(question_id=qid)
    datas = {}

    if choices:
        for r in choices:
            datas[r.choice_text] = r.votes
        result = json.dumps({'ststus':200, 'message':'success', 'data':datas})
        return HttpResponse(result)
    else:
        result = json.dumps({'ststus':10022, 'message':'Query result is empty'})
        return HttpResponse(result)


# 选择投票
def question_vote(request):

    qid = request.POST.get('qid', '')
    cid = request.POST.get('cid', '')

    if qid == '' or cid == '':
        result = json.dumps({'ststus':10021, 'message':'Parameter error'})
        return HttpResponse(result)

    choices = Choice.objects.filter(question_id=qid)

    if choices:
        try:
            p = get_object_or_404(Question, pk=qid)
            selected_choice = p.choice_set.get(pk=cid)
        except (KeyError, Choice.DoesNotExist):
            result = json.dumps({'ststus':10023, 'message':'The problem is not the choice id'})
            return HttpResponse(result)
        else:
            selected_choice.votes += 1
            selected_choice.save()
            result = json.dumps({'ststus':200, 'message':'success'})
            return HttpResponse(result)
    else:
        result = json.dumps({'ststus':10022, 'message':'Query result is empty'})
        return HttpResponse(result)
