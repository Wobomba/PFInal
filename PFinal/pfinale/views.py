from django.http import HttpResponse
from django.shortcuts import render
import joblib
import pandas as pd

cls = joblib.load('./models/newton_model.sav')

def home(request):
    return render(request,'home.html')

def home2(request):
    return render(request, 'home2.html')

def results(request):
    print(request)

    if request.method == 'GET':
        lis = {}
        lis['school']=request.GET.get('school_types')
        lis['sex']=request.GET.get('sex')
        lis['age']=request.GET.get('age')
        lis['address']=request.GET.get('address')
        lis['famsize']=request.GET.get('famsize')
        lis['Pstatus']=request.GET.get('Pstatus')
        lis['Fedu']=request.GET.get('Fedu')
        lis['Mjob']=request.GET.get('Mjob')
        lis['Fjob']=request.GET.get('Fjob')
        lis['reason']=request.GET.get('reason')
        lis['guardian']=request.GET.get('guardian')
        lis['traveltime']=request.GET.get('traveltime')
        lis['failures']=request.GET.get('failures')
        lis['schoolsup']=request.GET.get('schoolsup')
        lis['famsup']=request.GET.get('famsup')
        lis['activities']=request.GET.get('activities')
        lis['nursery']=request.GET.get('nursery')
        lis['higher']=request.GET.get('higher')
        lis['internet']=request.GET.get('internet')
        lis['romantic']=request.GET.get('romantic')
        lis['famrel']=request.GET.get('famrel')
        lis['freetime']=request.GET.get('freetime')
        lis['goout']=request.GET.get('goout')
        lis['Dalc']=request.GET.get('Dalc')
        lis['Walc']=request.GET.get('Walc')
        lis['health']=request.GET.get('health')
        lis['absences']=request.GET.get('absences')
        lis['passed']=request.GET.get('passed')

    testData = pd.DataFrame({'x':lis}).transpose
    prediction = cls.predict(testData)[0]
    context= {'prediction':'prediction'}
    return render(request, 'results.html', context)


