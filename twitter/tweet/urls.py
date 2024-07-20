from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),  # List all tweets
    path('tweet/new/', views.tweet_create, name='tweet_create'),  # Create new tweet
    path('tweet/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),  # Edit a specific tweet
    path('tweet/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),  # Delete a specific tweet
    path('register/', views.register, name='register')  # User registration
]
