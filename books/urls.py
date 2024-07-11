from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('upload/', views.upload_book, name='upload_book'),
]
