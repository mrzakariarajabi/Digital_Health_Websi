from django.contrib import admin 
from .models import diabetes_disease, ckd_disease, stroke_disease, cvd_disease

admin.site.register(diabetes_disease)
admin.site.register(ckd_disease)
admin.site.register(stroke_disease)
admin.site.register(cvd_disease)