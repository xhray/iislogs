from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from models import iis_logs, hit_stats
from forms import HitStatQueryForm
from datetime import datetime


def list(request):
    total = iis_logs.objects().count()
    entities = iis_logs.objects()
    return render_to_response('list.html', locals())


@csrf_exempt
def listhitstats(request):
    if request.method == 'POST':
        form = HitStatQueryForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['day']
            entities = hit_stats.objects().filter(
                id__year=date.year, id__month=str(date.month).zfill(2), id__day=str(date.day).zfill(2)).order_by('-value__count')
            return render(request, 'listhitstats.html', {'entities': entities, 'form': form})
    else:
        form = HitStatQueryForm()

    return render(request, 'listhitstats.html', {'form': form})
