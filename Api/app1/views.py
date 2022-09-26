from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render
from django.http import HttpResponse
import sys, json
import requests
from django.http import JsonResponse
from django.template.response import TemplateResponse



# Create your views here.
def capture_get(request):
    string1 = request.GET ['texto'] 
    return render(request, 'showResult.html',{'texto':string1})
def postdata(request):
    return render(request,'postData.html')
@csrf_exempt    
def showPost(request):
        string1 = request.POST['texto']
        data = {"texto":string1}
        url = 'http://zaira.ifrn.edu.br:8080'
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(url,json.dumps(data, indent=True),headers=headers)
        #todos=json.loads(response)
        todos=response.json()
        print(type(todos))
        print(todos)
        return render(request,'postData.html',{'texto':todos})    