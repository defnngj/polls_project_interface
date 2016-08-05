from django.shortcuts import get_object_or_404
from .models import Question, Choice
from django.http import JsonResponse


# Create your views here.
# 首页展示所有问题
def questions(request):
    question_list = Question.objects.all()
    datas = {}
    if question_list:
        for question in question_list:
            datas[question.id] = question.question_text
        return JsonResponse({'ststus':200, 'message':'success', 'data':datas})
    else:
        return JsonResponse({'ststus':10022, 'message':'Query result is empty'})


# 查看问题选项
def question_option(request):
    qid = request.GET.get('qid', '')
    if qid == '':
        return JsonResponse({'ststus':10021, 'message': 'Parameter error'})

    choices = Choice.objects.filter(question_id=qid)
    datas = {}

    if choices:
        for choice in choices:
            datas[choice.id] = choice.choice_text
        return JsonResponse({'ststus':200, 'message':'success', 'data':datas})
    else:
        return JsonResponse({'ststus':10022, 'message':'Query result is empty'})


# 查看问题的投票结果
def question_result(request):
    qid = request.GET.get('qid', '')
    if qid == '':
        return JsonResponse({'ststus':10021, 'message':'Parameter error'})

    choices = Choice.objects.filter(question_id=qid)
    datas = {}

    if choices:
        for r in choices:
            datas[r.choice_text] = r.votes
        return JsonResponse({'ststus':200, 'message':'success', 'data':datas})
    else:
        return JsonResponse({'ststus':10022, 'message':'Query result is empty'})


# 选择投票
def question_vote(request):

    qid = request.POST.get('qid', '')
    cid = request.POST.get('cid', '')

    if qid == '' or cid == '':
        return JsonResponse({'ststus':10021, 'message':'Parameter error'})

    choices = Choice.objects.filter(question_id=qid)

    if choices:
        try:
            p = get_object_or_404(Question, pk=qid)
            selected_choice = p.choice_set.get(pk=cid)
        except (KeyError, Choice.DoesNotExist):
            return JsonResponse({'ststus':10023, 'message':'The problem is not the choice id'})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return JsonResponse({'ststus':200, 'message':'success'})
    else:
        return JsonResponse({'ststus':10022, 'message':'Query result is empty'})
