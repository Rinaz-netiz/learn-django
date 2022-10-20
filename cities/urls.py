from django.urls import path
from cities.views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='city_detail_view'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='city_update_view'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='city_delete_view'),
    path('create/', CityCreateView.as_view(), name='city_create_view'),
]
