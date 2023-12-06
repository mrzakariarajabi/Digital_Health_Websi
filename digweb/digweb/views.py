from django.http import HttpResponse
from django.shortcuts import render

def mainpage(request):
    return render(request, "openVeiw/index.html")
    #return render(request, "hello/index.html")

def zakaria(request):
    return HttpResponse("Hello, zakaria!")