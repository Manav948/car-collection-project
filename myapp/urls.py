from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/', views.manage_order, name='manage_order'),
    path('orders/update/<int:order_id>/<str:status>/', views.update_order, name='update_order'),
    path('cars/', views.car_list, name='car_list'),
    path('collections/', views.collection_list, name='collection_list'),
    path('order/',views.order_page, name='order_page'),
]
