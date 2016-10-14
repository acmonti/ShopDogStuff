from django import forms

from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = {
            "image",
            "price",
            "stocks",
            "description",
            "name",
        }