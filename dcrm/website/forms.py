from django import forms
from .models import Product, Order, Sale

class AddProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"
class AddOrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields="__all__"

class AddSale(forms.ModelForm):
    class Meta:
        model= Sale
        fields= "__all__"

class AddCartForm(forms.Form):
    product_id=forms.IntegerField()
    quantity=forms.IntegerField()
    


