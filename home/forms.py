from django import forms
from .models import Product, Category
from tinymce.widgets import TinyMCE

class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20}))
    class Meta:
        model = Product
        fields = (
            'name',
            'img',
            'barcode',
            'category',
            'price',
            'description',
            'is_featured',
        )
