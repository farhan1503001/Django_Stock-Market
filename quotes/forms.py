from django import forms
from django.forms import Form,fields
from .models import Stock

class Stock_form(forms.ModelForm):
    class Meta:
        model=Stock
        fields=["stock_item"]