from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_root),
    path('freighters/',
         views.FreighterList.as_view(),
         name='freighter-list'),
    path('freighters/<int:pk>/',
         views.FreighterCompany.as_view()),
]