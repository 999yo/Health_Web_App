from django import forms
from django.shortcuts import render
from . import forms
from django.template.context_processors import csrf

def check(request):
    labels = ['呼吸苦']
    results ={}
    ret = ''
    if request.method == 'POST':
        results[labels[0]] = request.POST.getlist('zero')
        ret = 'OK'
        c = {'results': results, 'ret': ret}
    
    else:
        form = forms.HealthCheck()
        choice1 = []
        c = {'form': form,'ret':ret}
        c.update(csrf(request))
    return render(request, 'health_care.html',c)
