from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create, name = 'create'),
    #path('/', views.home, name = 'home'),
    path('<int:meeting_id>', views.detail, name = 'detail'),
    path('<int:meeting_id>/attend', views.attend, name = 'attend'),
]
