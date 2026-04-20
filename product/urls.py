from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list_create, name='product-list-create'),
    path('products/<int:pk>/', views.product_detail_update_delete, name='product-detail-update-delete'),
]
