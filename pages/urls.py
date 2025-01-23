from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts', views.posts, name='posts'),
    path('notifications', views.notifications, name='notifications'),
    path('messages', views.messages, name='messages'),
    path('analytics', views.analytics, name='analytics'),
]