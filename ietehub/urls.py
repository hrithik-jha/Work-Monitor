from django.contrib import admin
from django.urls import path, include
from meetings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('accounts/', include('accounts.urls')),
    path('meetings/', include('meetings.urls')),
    path('chat/', include('chat.urls')),
]
