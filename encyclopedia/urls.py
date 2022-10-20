from django.urls import path, include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),

    path('fish_all/', views.getAllFish),
    path('get_fish/<str:pk>/', views.getFishInfo),
    path('add_fish/', views.addFishInfo),
    path('update_fish/<str:pk>/', views.updateFishInfo),
    path('delete_fish/<str:pk>/', views.deleteFishInfo),

    path('regions/', views.getRegionInfo),

    path('staff/<str:pk>/', views.getStaff),

    path('add_message/', views.createMessage),
    path('get_message_all/', views.getAllMessages),
    path('get_message/<str:pk>/', views.viewMessage),
    path('delete_message/<str:pk>/', views.deleteMessage),


]