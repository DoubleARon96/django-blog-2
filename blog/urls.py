from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # this is an exsample of url change = path('posts/', views.PostList.as_view(), name='home'),
]