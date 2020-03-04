from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def chartjs(request):
    return render(request, 'chartjs.html')


@login_required
def echarts(request):
    return render(request, 'echarts.html')
