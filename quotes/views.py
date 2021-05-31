from django.shortcuts import render
from .models import Stock
# Create your views here.

def home(request):
    import requests
    import json 
    #API KEY: 6AtfJj3itkxGv1VKfZSNZUA8DGcxiWj4ijXOmaRY0dC5wiBDPJctHSKv3sae
    #ticker_url=https://api.polygon.io/v2/reference/tickers?sort=ticker&perpage=100&page=1&apiKey=5fVKgjYXxOtadkAmuRAtgC0n1DZU_qGO
    #url='https://mboum.com/api/v1/qu/quote/?symbol=AAPL,F&apikey=6AtfJj3itkxGv1VKfZSNZUA8DGcxiWj4ijXOmaRY0dC5wiBDPJctHSKv3sae'
    if request.method=='POST':
        ticker_name=request.POST['ticker']
        url='https://mboum.com/api/v1/qu/quote/?symbol='+ticker_name+'&apikey=6AtfJj3itkxGv1VKfZSNZUA8DGcxiWj4ijXOmaRY0dC5wiBDPJctHSKv3sae'
        response=requests.get(url=url)
        if response:
            api=json.loads(response.content)
        else:
            api='ERROR'
        return render(request,'home.html',{'data':api})
    else:
        url='https://mboum.com/api/v1/qu/quote/?symbol=AAPL&apikey=6AtfJj3itkxGv1VKfZSNZUA8DGcxiWj4ijXOmaRY0dC5wiBDPJctHSKv3sae'
        response=requests.get(url=url)
        if response:
            api=json.loads(response.content)
        else:
            api='ERROR'
        return render(request,'home.html',{'data':api})
def about(request):
    return render(request,'about.html',{})
def add_stock(request):
    ticker_name=Stock.objects.all()
    return render(request,'add_stock.html',{'stock_name':ticker_name})