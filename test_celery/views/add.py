#__*__coding:utf-8__*__

from celery.result import AsyncResult
from django.shortcuts import render_to_response

from tools.tasks import plus_1, multi_1
from test_celery.models import Plus, Multi
from tools.db import Db
import datetime


def index(request):
    return  render_to_response('index.html')

def multiIndex(request):
    return  render_to_response('multiIndex.html')


def plus(request):
    first = int(request.GET.get('first'))
    second = int(request.GET.get('second'))
    result = plus_1.delay(first,second)
    dd = Plus(task_id=result.id,first=first,second=second,log_date=datetime.datetime.now())
    dd.save()
    return render_to_response('index.html')

def multi(request):
    multiplier = int(request.GET.get('multiplier'))
    multiplicand = int(request.GET.get('multiplicand'))
    result = multi_1.delay(multiplier,multiplicand)
    dd = Multi(task_id=result.id,multiplier=multiplier,multiplicand=multiplicand,log_date=datetime.datetime.now())
    dd.save()
    return render_to_response('multiIndex.html')

# 任务结果
def results(request):
    #查询所有的任务信息
    db = Db()
    rows = db.get_tasksinfo()
    return render_to_response('result.html', {'rows':rows})

# 任务结果
def multiResults(request):
    #查询所有的任务信息
    db = Db()
    rows = db.get_MultiTasksinfo()
    return render_to_response('multiResults.html', {'rows':rows})