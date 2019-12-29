from django.http import HttpResponse
from django.shortcuts import render

from products.models import Product
from django.db.models import Q
# Create your views here.


def search_list_view(request):
    query = request.GET.get('q')
    if query:
        qs = Product.objects.search(query)
        context = {
            'object_list': qs
        }
        if qs:
            return render(request, "products/list.html", context)
    return HttpResponse("<h1> Sorry no Product found !!! </h1>")
