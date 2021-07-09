from typing_extensions import SupportsIndex
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import InputForm
import pandas as pd
import numpy as np
import pickle
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['PatientDB']


loaded_model = pickle.load(open("C:/Users/Kyle/Untitled Folder/finalized_model.pkl", 'rb'))

def index(request):
    if request.method == "POST":
        myform = InputForm(request.POST)
        if myform.is_valid():
            age = myform.cleaned_data['age_v']
            sex = myform.cleaned_data['sex_v']

            cp = myform.cleaned_data['cp_v']
            thalach = myform.cleaned_data['thalach_v']
            exang = myform.cleaned_data['exang_v']
            oldpeak = myform.cleaned_data['oldpeak_v']
            slope = myform.cleaned_data['slope_v']

            ca = myform.cleaned_data['ca_v']

            m_inputs = [[age, sex, cp, thalach, exang, oldpeak, slope, ca]]
            

            y_pred = [np.exp(point)/np.sum(np.exp(point), axis=0)
                for point in m_inputs]

            
            return render(request, 'index.html', {'prediction': round(y_pred.mean())})


    else:
        myform = InputForm()

  

    return render(request, 'index.html', {'form': myform})

def updateDataBase(request):
      temp={}
      
      temp['age']= myform.cleaned_data['age_v']
      temp['sex']= myform.cleaned_data['sex_v']
      temp['cp']= myform.cleaned_data['cp_v']
      temp['thalach']= myform.cleaned_data['thalach_v']
      temp['exang']= myform.cleaned_data['exang_v']
      temp['oldpeak']= myform.cleaned_data['oldpeak_v']
      temp['slope']= myform.cleaned_data['slope_v']
      temp['ca']= myform.cleaned_data['ca_v']
      
      collectionD.insert_one(temp)
      countOfrow = collectionD.find().count()
      context = {"Row Count": countOfrow}
      
      return render(request,'viewDB.html',context)
      
        


    
