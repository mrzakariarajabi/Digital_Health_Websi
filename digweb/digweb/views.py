from django.http import HttpResponse
from django.shortcuts import render

def mainpage(request):
    return render(request, "openVeiw/index.html")
    #return render(request, "hello/index.html")

def mainpr_page(request):
    return render(request, "persianPage/indexpr.html")

def zakaria(request):
    return HttpResponse("Hello, zakaria!")

def about_page(request):
    return render(request, "openVeiw/about.html")

def aboutpr_page(request):
    return render(request, "persianPage/aboutpr.html")

def appointment_page(request):
    return render(request, "openVeiw/appointment.html")

def service_page(request):
    return render(request, "openVeiw/service.html")

def servicepr_page(request):
    return render(request, "persianPage/servicepr.html")

def diabetes_page(request):
    return render(request, "openVeiw/diabetes.html")

def diabetespr_page(request):
    return render(request, "persianPage/diabetespr.html")

def stroke_page(request):
    return render(request, "openVeiw/stroke.html")

def strokepr_page(request):
    return render(request, "persianPage/strokepr.html")

def ckd_page(request):
    return render(request, "openVeiw/ckd.html")

def ckdpr_page(request):
    return render(request, "persianPage/ckdpr.html")

def cvd_page(request):
    return render(request, "openVeiw/cvd.html")

def cvdpr_page(request):
    return render(request, "persianPage/cvdpr.html")

def under_page(request):
    return render(request, "error/UnderConstruction.html")

def error_404_handler(request, exception):
    return render(request, "error/page404.html")