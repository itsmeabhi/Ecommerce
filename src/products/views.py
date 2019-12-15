# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Product

# Create your views here.


def product_list_view(request):
    qs = Product.objects.all()
    context = {
        'qs': qs
    }
    return render(request, "products/list.html", context)

