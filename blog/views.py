from django.shortcuts import render

# Create your views here.
def blog(request):
    datas = {

    }
    return render(request,"pages/blog.html",datas)

def single_blog(request):
    datas = {

    }
    return render(request,"pages/single-blog.html",datas)
