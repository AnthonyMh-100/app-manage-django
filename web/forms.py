from django import forms
from .models import Product,Customer

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'bg-gray-600 text-white border-none focus:ring-2 focus:ring-purple-600 w-full p-2 rounded',
                'placeholder': 'Nombre'
            }),
            'description': forms.Textarea(attrs={
                'class': 'bg-gray-600 text-white border-none focus:ring-2 focus:ring-purple-600 w-full p-2 rounded',
                'placeholder': 'Descripción'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'bg-gray-600 text-white border-none focus:ring-2 focus:ring-purple-600 w-full p-2 rounded',
                'placeholder': 'Precio'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'bg-gray-600 text-white border-none focus:ring-2 focus:ring-purple-600 w-full p-2 rounded',
                'placeholder': 'Stock'
            }),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'last_name', 'age', 'email','phone']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'bg-gray-600 text-white border-none focus:ring-2 focus:ring-purple-600 w-full p-2 rounded',
                'placeholder': 'Nombre'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'bg-gray-600 text-white border-none focus:ring-2 focus:ring-purple-600 w-full p-2 rounded',
                'placeholder': 'Apellido'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'bg-gray-600 text-white border-none focus:ring-2 focus:ring-purple-600 w-full p-2 rounded',
                'placeholder': 'Edad'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'bg-gray-600 text-white border-none focus:ring-2 focus:ring-purple-600 w-full p-2 rounded',
                'placeholder': 'Correo'
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'bg-gray-600 text-white border-none focus:ring-2 focus:ring-purple-600 w-full p-2 rounded',
                'placeholder': 'Phone'
            }),
            
        }