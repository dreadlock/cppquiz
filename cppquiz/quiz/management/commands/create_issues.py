import json
import urllib2

from django.core.management.base import BaseCommand
from cppquiz.quiz.models import Question
from django.db.models import Q
from . import text_generator

class Command(BaseCommand):


    def add_arguments(self, parser):
        parser.add_argument('user', nargs=1)
        parser.add_argument('repo', nargs=1)
        parser.add_argument('token', nargs=1)

    def handle(self, *args, **options):
        for q in Question.objects.filter(Q(state='PUB') | Q(state='ACC')):
            print("Creating issue for " + str(q.id))
            title = 'Update question ' + str(q.id)
            body = text_generator.get_issue(q)
            data = json.dumps({'issue' : {'title' : title, 'body' : body}})
            url = 'https://api.github.com/repos/' + options['user'][0] + '/' + options['repo'][0] + '/import/issues'
            headers = {
                'Authorization' : 'token ' + options['token'][0],
                'Accept' : 'application/vnd.github.golden-comet-preview+json'
            }
            request = urllib2.Request(url, data, headers)
            response=urllib2.urlopen(request)
            print(response.read())
