__author__ = 'fnngj'
from django.conf.urls import url
from polls import views

urlpatterns = [
    # ex : /polls/questions/
    url(r'^questions/$', views.questions, name='questions'),
    # ex : /polls/question_option/
    url(r'^question_option/$', views.question_option, name='question_option'),
    # ex : /polls/question_result/
    url(r'^question_result/$', views.question_result, name='question_result'),
    # ex : /polls/question_vote/
    url(r'^question_vote/$', views.question_vote, name='question_vote'),
]
