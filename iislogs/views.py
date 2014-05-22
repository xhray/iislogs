# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import iis_logs, hit_stats
from forms import HitStatQueryForm
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import cStringIO

def list(request):
    total = iis_logs.objects().count()
    entities = iis_logs.objects()
    return render_to_response('list.html', locals())


@csrf_exempt
def listhitstats(request):
    if request.method == 'POST':
        form = HitStatQueryForm(request.POST)
        if form.is_valid():
            record_limit = 10
            date = form.cleaned_data['day']
            entities = hit_stats.objects().filter(id__year=date.year, id__month=str(date.month).zfill(2), id__day=str(date.day).zfill(2)).order_by('-value__count').limit(record_limit)

            fig = Figure(figsize=(15, 25))
            ax = fig.add_subplot(111)
            ax.bar(np.arange(len(entities)), map(lambda x : x.value['count'], entities), alpha=0.4)
            ax.set_xticks(np.arange(record_limit))
            ax.set_xticklabels(map(lambda x: x.id['url'], entities), rotation=60)
            ax.set_title('sfa hit stats : {0}'.format(date))
            canvas = FigureCanvas(fig)

            buf = cStringIO.StringIO()
            canvas.print_png(buf, format='png')
            chart = buf.getvalue().encode('base64').strip()

            return render(request, 'listhitstats.html', {'entities':entities, 'form':form, 'chart':chart})
    else:
        form = HitStatQueryForm()

    return render(request, 'listhitstats.html', {'form': form})