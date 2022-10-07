from django.urls import path, include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),

    path('fish/', views.getAllFish),
    path('get/<str:pk>/', views.getFishInfo),
    path('add/', views.addFishInfo),
    path('update/<str:pk>/', views.updateFishInfo),
    path('delete/<str:pk>/', views.deleteFishInfo),

    path('regions/', views.getRegionInfo),
]