from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainpage, name='main'),
    path('account/', views.accountpage, name='account'),
    path('events/', views.eventspage, name='events'),
    path('talktous/', views.talk_to_us, name='talktous'),
    path('posts/', views.posts, name='posts'),
    path('books/', views.books, name='books'),
    path('archieve/', views.archieve, name='archieve'),
    path('poets/', views.poets, name='poets'),
    path('just/', views.just, name='just'),
 ]