from django.shortcuts import render

# Create your views here.

def Abu(request):
    return render(request,'sor/Aboutus.html')

def Blo(request):
    return render(request,'sor/Blog.html')
