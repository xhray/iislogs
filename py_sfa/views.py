from django.http import HttpResponse

def hello(request):
    return HttpResponse('test')

from django.shortcuts import render_to_response

def test(request):
    name = 'zzzz'
    age = 20

    return render_to_response('test.html', locals())

