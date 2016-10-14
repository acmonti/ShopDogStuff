from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .forms import ProductForm

from .models import *

# Create your views here.
def new_product (request):
    template = loader.get_template('form.html')
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Product successfully added!")
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

def index (request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def shop (request):
    template = loader.get_template('shop.html')
    context = {
        #'categories': Category.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def detail (request, id=None):
    instance = get_object_or_404(Clothes, id=id)
    template = loader.get_template('detail.html')
    context = {
        'instance': instance
    }
    return HttpResponse(template.render(context, request))

def clothes (request):
    template = loader.get_template('clothes.html')
    queryset = Clothes.objects.all()
    context = {
        'product_list': queryset
    }
    return HttpResponse(template.render(context, request))

