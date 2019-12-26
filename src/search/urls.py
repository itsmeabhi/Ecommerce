from django.urls import path

from .views import search_list_view

app_name = 'search'  # Required for namespace in path for URLS reverse routing.
urlpatterns = [
    path('', search_list_view, name='search'),
]
