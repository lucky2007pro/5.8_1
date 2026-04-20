from django.urls import path
from . import views

urlpatterns = [
    path('shops/', views.shop_list_create, name='shop-list-create'),
    path('shops/<int:pk>/', views.shop_detail_update_delete, name='shop-detail-update-delete'),
]
