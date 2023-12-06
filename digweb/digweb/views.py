from django.http import HttpResponse
from django.shortcuts import render

def mainpage(request):
    return render(request, "openVeiw/index.html")
    #return render(request, "hello/index.html")

def zakaria(request):
    return HttpResponse("Hello, zakaria!")

def about_page(request):
    return render(request, "openVeiw/about.html")

def appointment_page(request):
    return render(request, "openVeiw/appointment.html")

def service_page(request):
    return render(request, "openVeiw/service.html")
