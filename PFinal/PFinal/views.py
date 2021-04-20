from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,'home.html')

def home2(request):
    return render(request, 'home2.html')

def results(request):
    cls = joblib.load(open('newton_model.sav'))

    lis = []
    lis.append(request.GET['school_types'])
    lis.append(request.GET['sex'])
    lis.append(request.GET['age'])
    lis.append(request.GET['address'])
    lis.append(request.GET['famsize'])
    lis.append(request.GET['Pstatus'])
    lis.append(request.GET['Medu'])
    lis.append(request.GET['Fedu'])
    lis.append(request.GET['Mjob'])
    lis.append(request.GET['Fjob'])
    lis.append(request.GET['Reason'])
    lis.append(request.GET['gaurdian'])
    lis.append(request.GET['traveltime'])
    lis.append(request.GET['studytime'])
    lis.append(request.GET['failures'])
    lis.append(request.GET['schoolsup'])
    lis.append(request.GET['famsup'])
    lis.append(request.GET['paid'])
    lis.append(request.GET['activities'])
    lis.append(request.GET['nursery'])
    lis.append(request.GET['schoolsup1'])
    lis.append(request.GET['internet'])
    lis.append(request.GET['romantic'])
    lis.append(request.GET['famrel'])
    lis.append(request.GET['freetime'])
    lis.append(request.GET['goout'])
    lis.append(request.GET['Dalc'])
    lis.append(request.GET['health'])
    lis.append(request.GET['absences'])
    lis.append(request.GET['passed'])

    print(lis)
    
    return render(request, 'results.html')

