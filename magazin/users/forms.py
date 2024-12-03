from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'patronymic', 'age', 'about', 'photo', 'password']

from django import forms
from .models import Product

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'condition', 'characteristics', 'photo']
# users/forms.py
from django import forms

class ProductSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Поиск товара')

