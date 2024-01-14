from django.http import HttpResponse
from django.shortcuts import render
from .models import diabetes_disease, cvd_disease, stroke_disease, ckd_disease
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

def create_diabetes(request):
    if request.method =='POST':
        id_number = request.POST.get('inputidnumber',False)
        age=request.POST.get('inputDiabetesAge',False)
        weight=request.POST.get('inputDiabetesWeight', False)
        height=request.POST.get('inputPatientHeight', False)
        waist=request.POST.get('inputPatientWaist', False)
        gender=request.POST.get('inputPatientGender', False)
        druge_history=request.POST.get('inputPatientDrugHistory')
        vegetabls=request.POST.get('inputPationtVegetables') 
        His_family_glucose=request.POST.get('inputPationtGlucose')
        #PationtPhysicalActivity=request.POST.get('PationtPhysicalActivity')
        new_patient_diabetes=diabetes_disease(id_number=id_number,age=age,height=height,
                                              weight=weight,waist=waist,gender=gender,
                                              druge_history=druge_history,vegetabls=vegetabls,
                                              His_family_glucose=His_family_glucose)
        
        new_patient_diabetes.save()
        return HttpResponse()

def create_cvd(request):
    if request.method =='POST':
        id_number = request.POST.get('inputidnumber',False)
        age=request.POST.get('inputPatientAge',False)
        gender=request.POST.get('inputPatientGender', False)
        sbp_number=request.POST.get('inputPatientSBP', False)
        waist=request.POST.get('inputPatientWaist', False)
        hip=request.POST.get('inputPatientHip', False)
        smoke=request.POST.get('inputPationtSmoke')
        diabetes=request.POST.get('inputPationtDiabetes') 

        new_patient_cvd=cvd_disease(id_number=id_number,age=age,gender=gender,
                                              sbp_number=sbp_number,waist=waist,hip=hip,
                                              smoke=smoke,diabetes=diabetes)
 
        
        new_patient_cvd.save()
        return HttpResponse()
    
def create_stroke(request):
    if request.method =='POST':
        id_number = request.POST.get('inputidnumber',False)
        age=request.POST.get('inputPatientAge',False)
        sbp_number=request.POST.get('inputPatientSBPHistory', False)
        gender=request.POST.get('inputPatientGender', False)
        related_medicine=request.POST.get('inputPatientDrugHistory')
        diabetes=request.POST.get('inputPatientDiabetes')
        smoke=request.POST.get('inputPationtSmoke')
        CVD_disease=request.POST.get('inputPationtCVD') 
        AF_disease=request.POST.get('inputPationtAF') 
        LVH_disease=request.POST.get('inputPationtLVH') 

        new_patient_stroke=stroke_disease(id_number=id_number,age=age,gender=gender,
                                              sbp_number=sbp_number,related_medicine=related_medicine,diabetes=diabetes,
                                              smoke=smoke,CVD_disease=CVD_disease,AF_disease=AF_disease,LVH_disease=LVH_disease)
 
        
        new_patient_stroke.save()
        return HttpResponse()

def create_ckd(request):
    if request.method =='POST':
        id_number = request.POST.get('inputidnumber',False)
        age=request.POST.get('inputPatientAge',False)
        gender=request.POST.get('inputPatientGender', False)
        anemia=request.POST.get('inputPatientAnemia')
        druge_history=request.POST.get('inputPatientDrugHistory')
        hypertention=request.POST.get('inputPatientHypertension')
        proteinuria=request.POST.get('inputPationtProteinuria')
        His_cvd=request.POST.get('inputPationtHistoryCVD') 
        His_CHF=request.POST.get('inputPationtHistoryCHF') 
        vascular_disease=request.POST.get('inputPationtPVD') 
        diabetes_mellitus=request.POST.get('inputPationtDM') 


        new_patient_ckd=ckd_disease(id_number=id_number,age=age,gender=gender,proteinuria=proteinuria,
                                    anemia=anemia,druge_history=druge_history,hypertention=hypertention,
                                    His_cvd=His_cvd,His_CHF=His_CHF,vascular_disease=vascular_disease,diabetes_mellitus=diabetes_mellitus)
 
        
        new_patient_ckd.save()
        return HttpResponse()
def error_404_handler(request, exception):
    return render(request, "error/page404.html")