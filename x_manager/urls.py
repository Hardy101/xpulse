from django.urls import path
from . import views

urlpatterns = [
    path('posts', views.fetch_posted_tweets, name='fetch_posted_tweets'),
]