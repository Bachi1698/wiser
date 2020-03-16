from django.shortcuts import render

# Create your views here.
def Event(request):
    datas = {

    }
    return render(request,"pages/Event.html",datas)

def event_details(request):
    datas = {

    }
    return render(request,"pages/event_details.html",datas)

def Admissions(request):
    datas = {

    }
    return render(request,"pages/Admissions.html",datas)

def courses(request):
    datas = {

    }
    return render(request,"pages/Courses.html",datas)

