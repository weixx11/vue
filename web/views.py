# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers

from django.views.decorators.http import require_http_methods
from web.models import Todos
import json


def getREQUEST(request):
    if request.method == 'POST':
        return request.POST
    elif request.method == 'GET':
        return request.GET

#/add
def add(request):
    res={}
    requestData=getREQUEST(request)
    print requestData
    print requestData['name']
    Todos.objects.create(content=requestData['name'])
    return HttpResponseRedirect('http://127.0.0.1/index.html')

#/delete
def delete(request):
    res={}
    requestData=getREQUEST(request)
    print requestData
    id=requestData['id']
    Todos.objects.filter(id=id).delete()
    return  HttpResponseRedirect('http://127.0.0.1/index.html')


#/index
def index(request):
    res={}
    todos = Todos.objects.all()
    res['data']=json.loads(serializers.serialize("json", todos))
    return  render(request, '../index.html', res)

#/show
def show(request):
    res={}
    todos = Todos.objects.all()
    res['data']=json.loads(serializers.serialize("json", todos))
    response=json.dumps(res)
    response = HttpResponse(response)
    response.__setitem__('Access-Control-Allow-origin', '*')
    response.__setitem__('Access-Control-Allow-Headers', 'x-requested-with,content-type')
    return  response