from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from .models import diabetes_disease, cvd_disease, stroke_disease, ckd_disease, alzheimer_disease
import xgboost as xgb
import pandas as pd
import json
import os


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

def dissai_page(request):
    return render(request,"openVeiw/dissai.html")

def dissaipr_page(request):
    return render(request,"persianPage/dissaipr.html" )

def digitalhealth_page(request):
    return render(request,'openVeiw/digitalhealth.html')

def digitalhealthpr_page(request):
    return render(request, "persianPage/digitalhealthpr.html")

def disscuseffect_page(request):
    return render(request, "openVeiw/disscuseffect.html")

def disscuseffectpr_page(request):
    return render(request, "persianPage/disscuseffectpr.html")

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

def alzheimer_page(request):
    return render(request, "openVeiw/alzheimer.html")

def alzheimerpr_page(request):
    return render(request, "persianPage/alzheimerpr.html")


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
                                              His_family_glucose=His_family_glucose,)
        
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
    

def create_alzheimer(request):
    if request.method =='POST':
        id_number = request.POST.get('inputidnumber',False)
        age=request.POST.get('inputPatientAge',False)
        weight=request.POST.get('inputPatientWeight', False)
        height=request.POST.get('inputPatientHeight', False)
        Education=request.POST.get('inputPatientEducation', False)
        gender=request.POST.get('inputPatientGender', False)
        SBP=request.POST.get('inputPatientSBP', False)
        Cholesterol=request.POST.get('inputPatientCholesterol')
        Activity=request.POST.get('inputPationtPhysicalActivity') 

        new_patient_diabetes=alzheimer_disease(id_number=id_number,age=age,height=height,
                                              weight=weight,Education=Education,gender=gender,
                                              SBP=SBP,Cholesterol=Cholesterol,
                                              Activity=Activity,)
        
        new_patient_diabetes.save()
        return HttpResponse()
    
################# HIV part #################
# Load the model
# Print the current working directory
print("Current Working Directory:", os.getcwd())

# Construct the path to the model file
model_path = os.path.join(os.getcwd(), 'digweb' ,'Static', 'model', 'model.json')

# Check if the file exists
if os.path.exists(model_path):
    loaded_model = xgb.Booster()
    loaded_model.load_model(model_path)
    print("Model loaded successfully.")
else:
    print(f"Model file not found at {model_path}")

feature_names = ['Gender', 'Prison record', 'Addiction record',
                 'Martial status', 'Occupation', 'Drug injection', 
                 'Sex inexchange for goods', 'Spouse of HIV person',
                 'Receiving Blood', 'Spouse of high-risk person', 'Unsafe behaviours', 'Age category']

def hiv_page(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            print("Received data:", body)  # Print the received data

            feature_names = [
                'Gender', 'Prison record', 'Addiction record', 'Martial status', 
                'Occupation', 'Drug injection', 'Sex inexchange for goods', 
                'Spouse of HIV person', 'Receiving Blood', 'Spouse of high-risk person', 
                'Unsafe behaviours', 'Age category'
            ]
            
            df = pd.DataFrame([body], columns=feature_names)
            #print("DataFrame:", df)  # Print the DataFrame

            dtest = xgb.DMatrix(df)
            predictions = loaded_model.predict(dtest)

            return JsonResponse({'prediction': float(predictions[0])})
        except Exception as e:
            #print(f"Error processing data: {e}")
            return JsonResponse({'error': 'Invalid data'}, status=400)
    else:
        return render(request, 'openVeiw/hiv.html')

#####################################################

def error_404_handler(request, exception):
    return render(request, "error/page404.html")