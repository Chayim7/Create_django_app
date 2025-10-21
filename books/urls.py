from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_reviews, name='all_reviews'),
    path('feed/', views.following_feed, name='following_feed'),
    path('books/', views.book_search, name='book_search'),
    path('books/new/', views.book_create, name='book_create'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/<int:pk>/review/new/', views.review_create, name='review_create'),
]
