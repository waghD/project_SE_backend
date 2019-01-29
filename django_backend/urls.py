"""django_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view
from django.views.generic.base import TemplateView
from .api import router
from logistics.views import FCUpdateView, FCCreateView, PlaneCreateView, PlaneUpdateView, TrainCreateView, \
    TrainUpdateView, TruckCreateView, TruckUpdateView

schema_view = get_swagger_view(title='Logistics Api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('freighter/edit/<int:pk>/', FCUpdateView.as_view(), name='fc_update'),
    path('freighter/add/', FCCreateView.as_view(), name='fc_create'),
    path('plane/add/,', PlaneCreateView.as_view(), name='plane_create'),
    path('train/add/,', TrainCreateView.as_view(), name='plane_create'),
    path('truck/add/,', TruckCreateView.as_view(), name='plane_create'),
    path('plane/edit/<int:pk>/', PlaneUpdateView.as_view(), name='plane_update'),
    path('train/edit/<int:pk>/', TrainUpdateView.as_view(), name='train_update'),
    path('truck/edit/<int:pk>/', TruckUpdateView.as_view(), name='truck_update'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('doc/', schema_view),
]

