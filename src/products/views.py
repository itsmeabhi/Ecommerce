# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render
from .models import Product

# Create your views here.


def product_list_view(request):
    qs = Product.objects.all()
    context = {
        'qs': qs
    }
    return render(request, "products/list.html", context)


def product_detail_view(request, pk=None):
    qs = Product.objects.get_by_id(pk)
    print(qs)
    if qs is None:
        raise Http404("product doesn't exist")
    context = {
        'qs': qs
    }
    return render(request, "products/detail.html", context)

