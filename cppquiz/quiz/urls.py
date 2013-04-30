from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


from quiz import views

urlpatterns = patterns('',
    url(r'^quiz/question/(?P<question_id>.*)', views.question, name='question'),
    url(r'^quiz/clear', views.clear, name='clear'),
    url(r'^quiz/random', views.random_question, name='random'),
    url(r'^quiz/created', direct_to_template, {'template': 'quiz/created.html'}),
    url(r'^quiz/create', views.create, name='create'),
    url(r'^quiz/about', direct_to_template, {'template': 'quiz/help.html'}),
    url(r'^quiz/help', direct_to_template, {'template': 'quiz/help.html'}),
    url(r'^$', views.index, name='index'),
)
