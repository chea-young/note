from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template("main.html")
    context = {
        
    } # template에 담을 데이터
    return HttpResponse(template.render(context, request))