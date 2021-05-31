from django.shortcuts import redirect, render
from .models import Stock
from .forms import Stock_form
from django.contrib import messages
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
    import requests
    import json
    if request.method=='POST':
        form=Stock_form(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'Ticker Added Successfully!')
            return redirect('add_stock')
    else:
        ticker_name=Stock.objects.all()
        dataset=list()
        for ticker in ticker_name:
            url='https://mboum.com/api/v1/qu/quote/?symbol='+str(ticker)+'&apikey=6AtfJj3itkxGv1VKfZSNZUA8DGcxiWj4ijXOmaRY0dC5wiBDPJctHSKv3sae'
            response=requests.get(url)
            try:
                api=json.loads(response.content)
                dataset.append(api)
            except Exception as e:
                api='ERROR'

        return render(request,'add_stock.html',{'stock_name':ticker_name,'dataset':dataset})

def delete(request,id):
    item=Stock.objects.get(pk=id)
    item.delete()
    messages.success(request,'Ticker Deleted Successfully')
    return redirect('add_stock')