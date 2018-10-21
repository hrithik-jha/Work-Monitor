from django.urls import path, include
from . import views

urlpatterns = [
    path('video/', views.home, name = 'chat'),
    path('text/', views.text, name = 'tchat'), 
    path('text/send/', views.send, name = 'send'),
]
