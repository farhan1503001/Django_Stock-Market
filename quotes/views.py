from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json 
    #API KEY: 6AtfJj3itkxGv1VKfZSNZUA8DGcxiWj4ijXOmaRY0dC5wiBDPJctHSKv3sae
    url='https://mboum.com/api/v1/qu/quote/?symbol=AAPL,F&apikey=6AtfJj3itkxGv1VKfZSNZUA8DGcxiWj4ijXOmaRY0dC5wiBDPJctHSKv3sae'
    response=requests.get(url=url)
    if response:
        api=json.loads(response.content)
    else:
        api='ERROR'
    return render(request,'home.html',{'data':api})
def about(request):
    return render(request,'about.html',{})
def add_stock(request):
    return render(request,'add_stock.html',{})