from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import random


@login_required
def tables(request):
    return render(request, 'tables.html')


@login_required
def tables_dynamic(request):
    return render(request, 'tables_dynamic.html')


@login_required
def pricing_tables(request):
    return render(request, 'pricing_tables.html')


@csrf_exempt
@login_required
def bootstrap_tables(request):
    if request.method == 'GET':
        return render(request, 'bootstrap_tables.html')

    elif request.method == 'POST':
        limit = int(request.POST.get('limit'))
        offset = int(request.POST.get('offset'))
        search = request.POST.get('search')
        limit = offset + limit
        if search:
            rows = [{
                "id": '{0}-{1}'.format(x, offset),
                "name": '{0}-王{1}'.format(search, random.randint(0, 100)),
                "sex": random.choice(['M', 'F']),
                "age": random.randint(13, 16),
                "address": '上海市徐汇区{0}弄xxxxxxx小区{1}号{2}0{3}室'.format(random.randint(1000, 10000),
                                                                    random.randint(10, 100),
                                                                    random.randint(1, 10), random.randint(1, 4)),
                "city": random.choice(['SH', 'NJ', 'WH']),
                "subject_info": [{'subject': '语文', 'score': 100}, {'subject': '数学', 'score': 80},
                                 {'subject': '英语', 'score': 90}],
                "total_score": 270,
            } for x in range(501)]
        else:
            rows = [{
                "id": '{0}-{1}'.format(x, offset),
                "name": '王{}'.format(random.randint(0, 100)),
                "sex": random.choice(['M', 'F']),
                "age": random.randint(13, 16),
                "address": '上海市徐汇区{0}弄xxxxxxx小区{1}号{2}0{3}室'.format(random.randint(1000, 10000),
                                                                    random.randint(10, 100),
                                                                    random.randint(1, 10), random.randint(1, 4)),
                "city": random.choice(['SH', 'NJ', 'WH']),
                "subject_info": [{'subject': '语文', 'score': 100}, {'subject': '数学', 'score': 80},
                                 {'subject': '英语', 'score': 90}],
                "total_score": 270,
            } for x in range(1501)]
        res = {'rows': rows[offset:limit], 'total': len(rows)}
        return JsonResponse(res, safe=False)
