from django.shortcuts import render
from django.conf import settings
import os
import pickle
import sklearn
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))

def home(request):
    pred_message = None
    if request.method == 'POST':
        age = int(request.POST['age'])
        sex = int(request.POST['sex'])
        cp = int(request.POST['cp'])
        trestbps = int(request.POST['trestbps'])
        chol = int(request.POST['chol'])
        fbs = int(request.POST['fbs'])
        restecg = int(request.POST['restecg'])
        thalach = int(request.POST['thalach'])
        exang = int(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = int(request.POST['slope'])
        ca = int(request.POST['ca'])
        thal = int(request.POST['thal'])

        pred = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if pred[0] == 0:
            pred_message = "The Person does not have a Heart Disease"
        else:
            pred_message = "The Person has Heart Disease"
            
    context = {
        "prediction": pred_message
    }


    return render(request, "index1.html", context)
