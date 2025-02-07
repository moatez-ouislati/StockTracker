from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StockItem, Category

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StockUpViewForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)
    class Meta:
        model = StockItem
        fields = ['name', 'quantity', 'category']
        # in ths fields i must add price and decs

 