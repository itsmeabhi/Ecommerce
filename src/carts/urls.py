from django.urls import path

from .views import cart_home

app_name = 'carts'  # Required for namespace in path for URLS reverse routing.
urlpatterns = [
    path('', cart_home, name='list'),

]
