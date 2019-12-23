from django.urls import path

from .views import product_detail_view, product_list_view

urlpatterns = [
    path('', product_list_view, name='list'),
    path('<slug:slug>/', product_detail_view, name='detail'),
]
