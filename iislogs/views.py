from django.shortcuts import render_to_response
from iislogs.models import *

def list(request):
    total = iis_logs.objects().count()
    entities = iis_logs.objects(url='/c/client/home/edit/702505')
    return render_to_response('list.html', locals())