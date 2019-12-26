from django.http import HttpResponse
from django.shortcuts import render

from products.models import Product
# Create your views here.


def search_list_view(request):
    query = request.GET.get('q')
    if query:
        qs = Product.objects.filter(title__icontains=request.GET.get('q')).all()
        context = {
            'object_list': qs
        }
        if qs:
            return render(request, "products/list.html", context)
    return HttpResponse("<p> Sorry no Product found !!! </p>")
