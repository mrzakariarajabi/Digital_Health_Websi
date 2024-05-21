from django.db import models
from django.core.validators import MaxValueValidator


class diabetes_disease(models.Model):
    id_number = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    height = models.IntegerField(validators=[MaxValueValidator(999)])
    waist = models.IntegerField(validators=[MaxValueValidator(999)])
    age = models.IntegerField(validators=[MaxValueValidator(999)])
    weight = models.IntegerField(validators=[MaxValueValidator(999)])
    gender = models.BooleanField()
    druge_history = models.BooleanField()
    vegetabls  = models.BooleanField()
    His_family_glucose = models.BooleanField()
    #PationtPhysicalActivity = models.BooleanField()
    def __str__(self):
        return f"patiant with id number :{self.id_number}, age:{self.age},height :{self.height}, waist:{self.waist}, weight:{self.weight},gender:{self.gender}, druge history:{self.druge_history},vegetables:{self.vegetabls} His family glucose:{self.His_family_glucose}"
    
#############   ckd disease database   #############
class ckd_disease(models.Model):
    id_number = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    age = models.IntegerField(validators=[MaxValueValidator(999)])
    gender = models.BooleanField()
    anemia = models.BooleanField()
    druge_history = models.BooleanField()
    His_cvd = models.BooleanField()
    hypertention = models.BooleanField()
    proteinuria = models.BooleanField()
    vascular_disease = models.BooleanField()
    diabetes_mellitus = models.BooleanField()
    His_CHF = models.BooleanField()

    def __str__(self):
        return f"patiant with id number:{self.id_number}, age:{self.age},gender:{self.gender}, anemia:{self.anemia}, druge history:{self.druge_history},His cvd:{self.His_cvd}, hypertention:{self.hypertention}, proteinuria:{self.proteinuria},vascular disease:{self.vascular_disease}, diabetes mellitus:{self.diabetes_mellitus},history CHF:{self.His_CHF}"

#############   stroke disease database   #############

class stroke_disease(models.Model):
    id_number = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    sbp_number = models.IntegerField(validators=[MaxValueValidator(999)])
    age = models.IntegerField(validators=[MaxValueValidator(999)])
    gender = models.BooleanField()
    related_medicine = models.BooleanField()
    diabetes = models.BooleanField()
    smoke = models.BooleanField()
    CVD_disease = models.BooleanField()
    AF_disease = models.BooleanField()
    LVH_disease = models.BooleanField()

    def __str__(self):
        return f"patiant with id number:{self.id_number}, SBP:{self.sbp_number}, age:{self.age}, gender:{self.gender}, related medicine:{self.related_medicine},diabetes:{self.diabetes}, smoke:{self.smoke}, CVD:{self.CVD_disease},AF:{self.AF_disease}, LVH:{self.LVH_disease}"
    
#############   CVD disease database   #############

class cvd_disease(models.Model):
    id_number = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    age = models.IntegerField(validators=[MaxValueValidator(999)])
    gender = models.BooleanField()
    sbp_number = models.IntegerField(validators=[MaxValueValidator(999)])
    smoke = models.BooleanField()
    diabetes = models.BooleanField()
    waist = models.IntegerField(validators=[MaxValueValidator(999)])
    hip = models.IntegerField(validators=[MaxValueValidator(999)])

    def __str__(self):
        return f"pationt with id number:{self.id_number}, age:{self.age}, gender:{self.gender},sbp_number:{self.sbp_number}, smoke:{self.smoke},diabetes:{self.diabetes},waist:{self.waist},hip:{self.hip}"
    
    #############   alzheimer disease database   #############
class alzheimer_disease(models.Model):
    id_number = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    height = models.IntegerField(validators=[MaxValueValidator(999)])
    weight = models.IntegerField(validators=[MaxValueValidator(999)])
    age = models.IntegerField(validators=[MaxValueValidator(999)])
    SBP = models.IntegerField(validators=[MaxValueValidator(999)])
    Education = models.IntegerField(validators=[MaxValueValidator(9)])
    gender = models.BooleanField()
    Cholesterol = models.BooleanField()
    Activity  = models.BooleanField()

    def __str__(self):
        return f"patiant with id number :{self.id_number}, age:{self.age},height :{self.height}, SBP:{self.SBP}, weight:{self.weight},gender:{self.gender}, Education:{self.Education},Cholesterol:{self.Cholesterol} Activity:{self.Activity}"