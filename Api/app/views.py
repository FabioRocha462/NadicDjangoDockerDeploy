from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    html="Please <a href = getData> Escreva Aqui </a>"
    return HttpResponse(html)
def getData(request):
    return render(request,'getData.html')
def showResult(request):
    string1 = request.GET ['texto'] 
    return render(request, 'showResult.html',{'texto':string1})
  

      
       

# Create your views here.
