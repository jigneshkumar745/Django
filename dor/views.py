from django.shortcuts import render
from dor.models import Contactus
from dor.models import Internship
# Create your views here.

def Contact(request):
    if request.method == 'POST':
        mail=request.POST['mail']
        Name=request.POST['Name']
        Issue=request.POST['Issue']
        Whatsapp=request.POST['Whatsaap']
        Cont=request.POST['Cont']
        State=request.POST['State']
        print(Name,Issue,Whatsapp,Cont,State)
        solid=Contactus(mail=mail,Issue=Issue,Name=Name,Whatsapp=Whatsapp,Cont=Cont,State=State)
        solid.save()

    return render(request,'dor/Contactus.html')

def Internships(request):
    if request.method == 'POST':
        FirstName=request.POST['FirstName']
        LastName=request.POST['LastName']
        Email=request.POST['Email']
        Contactno=request.POST['Contactno']
        College=request.POST['College']
        InternField=request.POST['InternField']
        Learning=Internship(FirstName=FirstName,LastName=LastName,Email=Email,Contactno=Contactno,College=College,InternFiels=InternField)
        Learning.save()

    return render(request,'dor/Internship.html')
