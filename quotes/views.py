from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json
    #https://cloud.iexapis.com/stable/stock/IBM/financials?token=pk_45759c428bf9456ea345b2fd2fa809eb&period=annual 
    #API KEY: pk_45759c428bf9456ea345b2fd2fa809eb 
    response=requests.get('')
    if response:
        api=json.loads(response.content)
    else:
        api='ERROR....'
    return render(request,'home.html',{'data':api})
def about(request):
    return render(request,'about.html',{})