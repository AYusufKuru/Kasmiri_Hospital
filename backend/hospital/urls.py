# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.ItemListCreateAPIView.as_view(), name='item-list'),
    path('items/<int:pk>/', views.ItemDetailAPIView.as_view(), name='item-detail'),
]
