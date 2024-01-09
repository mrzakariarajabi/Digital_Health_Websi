// diabetes function 
function diabetes_Results(page_number)
{
  //inputDiabetesAge
  //inputPatientGender
  //inputPatientBMI
  //inputPatientWaist
  //inputPatientDrugHistory
  //inputPationtPhysicalActivity
  //inputPationtGlucose
  //inputPationtVegetables
  var referringPage = document.referrer;

  if (referringPage) {
    console.log("The user was referred from: " + referringPage);
  } else {
    console.log("The user was not referred by another page.");
  }
// Age 
    var Age = document.getElementById('inputDiabetesAge'),
      Age_value = Age.value;
    //console.log("Age" + Age_value);
// gender
    var Gender = document.getElementById('inputPatientGender'),
      Gender_value = Gender.value;
    //console.log("Gender" + Gender_value);
// BMI
    var Height = document.getElementById('inputPatientHeight'),
      Height_value = Height.value;
      var Weight = document.getElementById('inputDiabetesWeight'),
      Weight_value = Weight.value;
      BMI_value = Weight_value /(Math.pow((Height_value/100),2));

    //var PatientBMI = document.getElementById('inputPatientBMI'),
      //BMI_value = PatientBMI.value;
    console.log("BMI = " + BMI_value);
//Waist
    var PatientWaist = document.getElementById('inputPatientWaist'),
    Waist_value = PatientWaist.value;
    //console.log("Waist" + Waist_value);
//DrugHistory
    var DrugHistory = document.getElementById("inputPatientDrugHistory").checked;
    //console.log( DrugHistory);
//PhysicalActivity
    var PhysicalActivity = document.getElementById("inputPationtPhysicalActivity").checked;
    //console.log( PhysicalActivity);
//Glucose
    var Glucose = document.getElementById("inputPationtGlucose").checked;
    //console.log( Glucose);
//inputPationtVegetables
    var Vegetables = document.getElementById("inputPationtVegetables").checked;
    //console.log( Vegetables);

    //Age
    if (Age_value < 45){
            Age_risk = 0;
            Age_point = 0;
        }
    else if (Age_value >= 45 && Age_value < 54){
            Age_risk = 0.650;
            Age_point = 2;
        }
    else if (Age_value >= 55 && Age_value < 64){
            Age_risk = 0.940;
            Age_point = 3;
        }
    else {
            Age_risk = 0.940;
            Age_point = 3;
        }
    //BMI
    if (BMI_value <=25 ){
            BMI_risk =0
            BMI_point = 0
        }
    else if  (BMI_value > 25 && BMI_value <= 30){
            BMI_risk =  0.015
            BMI_point = 1
        }
    else{
            BMI_risk = 0.938
            BMI_point = 3
        }
    //Gender
    if (Gender_value==0){ //Male
      
        if (Waist_value < 94){
                Waist_risk = 0
                Waist_point = 0
            }
        else if (Waist_value < 102){
                 Waist_risk = 1.021
                 Waist_point = 3
            }
        else{
                 Waist_risk = 1.424
                 Waist_point =4
            }
        }
    else { //female
      
        if (Waist_value < 80){
                Waist_risk = 0
                Waist_point = 0
            }
        else if (Waist_value < 88){
                 Waist_risk = 1.021
                 Waist_point = 3
            }
        else{
                 Waist_risk = 1.424  
                 Waist_point = 4
            }
        }
// 
risk = Age_risk+BMI_risk+Waist_risk;
point = Age_point+ BMI_point+ Waist_point;
Risk_total = -5.658 + risk+ 0.714*DrugHistory+ 2.263*Glucose+ 0.268*PhysicalActivity+ 0.165*Vegetables;
point_total = point+ 2*DrugHistory + 5*Glucose + 2*PhysicalActivity+ 1*Vegetables;
final_Risk = Math.exp(Risk_total)/ (1+Math.exp(Risk_total));
console.log( "final_Risk = " + final_Risk);
if (page_number==1){
  document.getElementById("discribe_text").innerHTML = "ریسک 5 ساله شما برابر است با " + (final_Risk*100).toFixed(2)+" درصد";

}
else{
  document.getElementById("discribe_text").innerHTML = "your 5 year Risk equal by " + (final_Risk*100).toFixed(2)+" Percent.";

}


}
// end of diabetes function

// stroke function
function stroke_Results(page_number)
{
  //inputPatientAge
  //inputPatientGender
  //inputPatientDrugHistory
  //inputPatientSBPHistory
  //inputPatientDiabetes
  //inputPationtSmoke
  //inputPationtCVD
  //inputPationtAF
  //inputPationtLVH
  //inputPationtinteraction
  const year_man = [0.9948, 0.9889, 0.9826, 0.9740, 0.9642, 0.9551, 0.9422, 0.9270, 0.9144, 0.9044];
  const year_women = [0.9977, 0.9920, 0.9864, 0.9802, 0.9741, 0.9665, 0.9584, 0.9509, 0.9448, 0.9353];
  //Age
  var Age = document.getElementById('inputPatientAge'),
    Age_value = Age.value;
    //console.log("Age is " + Age_value);
  //DrugHistory
  var DrugHistory = document.getElementById("inputPatientDrugHistory").checked;
    //console.log( DrugHistory);
  //SBPHistory
  var SBPHistory = document.getElementById('inputPatientSBPHistory'),
    SBPHistory_value = SBPHistory.value;
    //console.log("Age is " + SBPHistory_value);
  //Diabetes
  var Diabetes = document.getElementById("inputPatientDiabetes").checked;
    //console.log( Diabetes);
  //Smoke
  var Smoke = document.getElementById("inputPationtSmoke").checked;
    //console.log( Smoke);
  //CVD
  var PationtCVD = document.getElementById("inputPationtCVD").checked;
    //console.log( PationtCVD);
  //AF
  var PationtAF = document.getElementById("inputPationtAF").checked;
    //console.log( PationtAF);
  //PationtLVH
  var PationtLVH = document.getElementById("inputPationtLVH").checked;
    //console.log( PationtLVH);
  //inputPationtinteraction
  PI_value =false;
  if (DrugHistory){
    if (SBPHistory_value >= 160){
      PI_value = true;
    }
    else{
      PI_value =false;
    }
  }
  //var Pationtinteraction = document.getElementById('inputPationtinteraction'),
    //PI_value = Pationtinteraction.value;
  
    //console.log( PI_value);
//year
var year = document.getElementById('year'),
    year_value = year.value;
    //console.log("The value is " + year_value);

//gender
    var gender = document.getElementById('inputPatientGender'),
        gender_value = gender.value;
    //console.log("The value is " + gender_value);
//////////////
      if (gender_value==1) {
        console.log("income");
        func_men = (0.0505*Age_value)+(0.0140*SBPHistory_value)+(0.3263*DrugHistory)+0.3384*Diabetes+0.5147*Smoke+0.5195*PationtCVD+0.6061*PationtAF+0.8415*PationtLVH;
        exp_men = func_men - 5.6670;
        f_men = Math.exp(exp_men);
        risk_men = 1-Math.pow(year_man[year_value-1], f_men);
        console.log("men = "+risk_men*100);
        if (page_number==1){
          document.getElementById("discribe_text").innerHTML = "ریسک " + year_value + " ساله شما برابر است با " + (risk_men*100).toFixed(2)+" درصد";
        }
        else{
          document.getElementById("discribe_text").innerHTML = "your " + year_value + " year Risk equal by " + (risk_men*100).toFixed(2)+" Percent.";
        }

      }
      else{
        func_women = (0.0657*Age_value)+(0.0197*SBPHistory_value)+(2.5432*DrugHistory)-0.0134*PI_value+0.5444*Diabetes+0.5294*Smoke+0.4326*PationtCVD+1.1497*PationtAF+0.8488*PationtLVH;
        exp_women = func_women - 7.5766;
        f_women = Math.exp(exp_women);
        risk_women = 1-Math.pow(year_women[year_value-1], f_women);
        console.log("women = "+risk_women*100);
        document.getElementById("discribe_text").innerHTML = "your " + year_value + " year Risk equal by " + (risk_women*100).toFixed(2)+" Percent.";

      }
}

// end of stroke function

// CKD function 
function ckd_Results(page_number)
{
  //inputPatientAge
  //inputPatientGender 
  //inputPatientAnemia
  //inputPatientDrugHistory
  //inputPatientHypertension
  //inputPationtHistoryCVD
  //inputPationtHistoryCHF
  //inputPationtPVD
  //inputPationtProteinuria
  //inputPationtDM
  // Age 
  var Age = document.getElementById('inputPatientAge'),
    Age_value = Age.value;
    if (Age_value <=49){
      //console.log("Age Categury 1");
      Age_cat1=1;Age_cat2=0;Age_cat3=0;Age_cat4=0;
    }
    else if (Age_value>=50 && Age_value<=59){
      //console.log("Age Categury 2");
      Age_cat1=0;Age_cat2=1;Age_cat3=0;Age_cat4=0;
    }
    else if (Age_value>=60 && Age_value<=69){
      //console.log("Age Categury 3");
      Age_cat1=0;Age_cat2=0;Age_cat3=1;Age_cat4=0;
    }
    else{
      //console.log("Age Categury 4");
      Age_cat1=0;Age_cat2=0;Age_cat3=0;Age_cat4=1;
    }
    // gender
    var Gender = document.getElementById('inputPatientGender'),
    Gender_value = Gender.value;
    //console.log("Gender" + Gender_value);
    // Anemia
    var Anemia = document.getElementById("inputPatientAnemia").checked;
          //console.log( Anemia);   
    // Drug History
    var DrugHistory = document.getElementById("inputPatientDrugHistory").checked;
          //console.log( DrugHistory); 
    // Hypertension
    var Hypertension = document.getElementById("inputPatientHypertension").checked;
          //console.log( Hypertension); 
    // HistoryCVD
    var HistoryCVD = document.getElementById("inputPationtHistoryCVD").checked;
          //console.log( HistoryCVD); 
    // HistoryCHF
    var HistoryCHF = document.getElementById("inputPationtHistoryCHF").checked;
          //console.log( HistoryCHF); 
    // PationtPVD
    var PationtPVD = document.getElementById("inputPationtPVD").checked;
          //console.log( PationtPVD); 
    // Proteinuria
    var Proteinuria = document.getElementById("inputPationtProteinuria").checked;
          //console.log( Proteinuria);
    //PationtDM
    var PationtDM = document.getElementById("inputPationtDM").checked;
          //console.log( PationtDM);
    //
  func_res=-5.4 +0*Age_cat1 +1.55*Age_cat2 + 2.31*Age_cat3 + 3.23*Age_cat4 + 0.29*Gender_value + 0.93*Anemia + 0.45*Hypertension + 0.44*PationtDM + 0.59*HistoryCVD + 0.45*HistoryCHF + 0.74*PationtPVD + 0.83*Proteinuria;
    exp_value=Math.exp(-func_res);
    Probability=1/(1+exp_value);
    console.log( Probability*100);
    if (page_number==1){
      document.getElementById("discribe_text").innerHTML = "ریسک 5 ساله شما برابر است با  " + (Probability*100).toFixed(2)+" درصد";
    }
    else{
      document.getElementById("discribe_text").innerHTML = "your 5 year Risk equal by " + (Probability*100).toFixed(2)+" Percent.";
    }
}

// end of CKD function

// CVD function 
function cvd_Results(page_number)
{
  //inputPatientAge
  //inputPatientGender 
  //inputPatientSBP
  //inputPatientWaist
  //inputPatientHip
  //inputPationtSmoke
  //inputPationtDiabetes
if (page_number==1){
  console.log(page_number);
}
  

  // Age 
  var Age = document.getElementById('inputPatientAge'),
    Age_value = Age.value;
  // gender
  var Gender = document.getElementById('inputPatientGender'),
    Gender_value = Gender.value;
    //console.log("Gender" + Gender_value);
  // SBP
  var PationtSBP = document.getElementById('inputPatientSBP'),
    SBP_value = PationtSBP.value;
  // Waist
  var Waist = document.getElementById('inputPatientWaist'),
    Waist_value = Waist.value;
  // Hip
  var Hip = document.getElementById('inputPatientHip'),
    Hip_value = Hip.value;
  // inputPationtSmoke
  var Smoke = document.getElementById("inputPationtSmoke").checked;
          //console.log( HistoryCVD); 
    // inputPationtDiabetes
  var Diabetes = document.getElementById("inputPationtDiabetes").checked;
          //console.log( HistoryCHF); 
    
    //SBP Value
  if (SBP_value>=120 && SBP_value<=139){
    sbpcat2=1;sbpcat3=0;sbpcat4=0;
    }
  else if (SBP_value>=140 && SBP_value<=159){
    sbpcat2=0;sbpcat3=1;sbpcat4=0;
    }
  else if (SBP_value>=160){
    sbpcat2=0;sbpcat3=0;sbpcat4=1;
    }
  else {
    sbpcat2=0;sbpcat3=0;sbpcat4=0;
    }
    // Gender
    WHR_Value = Waist_value/Hip_value;
      // WHR
    if (Gender_value == 1){
    
         if (WHR_Value>=0.85 && SBP_value<0.90){
            WHR_Value2=1;WHR_Value3=0;WHR_Value4=0;
          }
        else if (WHR_Value>=0.90 && WHR_Value<0.95){
            WHR_Value2=0;WHR_Value3=1;WHR_Value4=0;
          }
        else if (WHR_Value>=0.95){
            WHR_Value2=0;WHR_Value3=0;WHR_Value4=1;
          }
        else {//% i.e., WHR<0.85
            WHR_Value2=0;WHR_Value3=0;WHR_Value4=0;
        }
    }
    else{
        if (WHR_Value>=1 && SBP_value<1.05){
          WHR_Value2=1;WHR_Value3=0;WHR_Value4=0;
        }
        else if (WHR_Value>=1.05 && WHR_Value<1.10){
          WHR_Value2=0;WHR_Value3=1;WHR_Value4=0;
        }
        else if (WHR_Value>=1.10){
          WHR_Value2=0;WHR_Value3=0;WHR_Value4=1;
        }
        else{ //% i.e., WHR<1
           WHR_Value2=0;WHR_Value3=0;WHR_Value4=0;
          }

    }
      func_res=0.03823*(Age_value-50.69)+0.73001*(Diabetes-0.07)+0.47524*(sbpcat2-0.3534)+ 0.79045*(sbpcat3-0.1268)+1.13051*(sbpcat4-0.0730)+(-0.32309)*(Gender_value-0.51)+0.26560*(Smoke-0.22)+ 0.10478*(WHR_Value2-0.1291)+0.17986*(WHR_Value3-0.1414)+0.29440*(WHR_Value4-0.2384);



    exp_value=Math.exp(func_res);
    Probability=1-Math.pow(0.96303975,exp_value);
    console.log( Probability*100);
    if (page_number==1){
      document.getElementById("discribe_text").innerHTML = "ریسک 10 ساله شما برابر است با  " + (Probability*100).toFixed(2)+" درصد";
    }
    else{
      document.getElementById("discribe_text").innerHTML = "your 10 year Risk equal by " + (Probability*100).toFixed(2)+" Percent.";
    }
}

// end of CVD function