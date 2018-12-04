from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/', views.order_list),
    path('orders/<int:pk>/', views.order_detail)
]