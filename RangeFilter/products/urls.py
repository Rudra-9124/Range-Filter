from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('populate-products/', views.populate_products, name='populate_products'),
]