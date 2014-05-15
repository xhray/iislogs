from django.shortcuts import render_to_response
from iislogs.models import *

def list(request):
    total = iis_logs.objects().count()
    entities = iis_logs.objects()
    return render_to_response('list.html', locals())

def listhitstats(request):
	entities = hit_stats.objects().order_by('-value.count')
	return render_to_response('listhitstats.html', locals())