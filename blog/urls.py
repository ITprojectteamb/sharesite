from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/givelist/', views.give_list, name='give_list'),
    path('post/wantlist/', views.want_list, name='want_list'),
    path('post/givenew/', views.give_new, name='give_new'),
    path('post/wantnew/', views.want_new, name='want_new'),
    path('post/profilenew/', views.profile_new, name='profile_new'),
    path('post/givedetail/<int:pk>/', views.give_detail, name='give_detail'),
    path('post/wantdetail/<int:pk>/', views.want_detail, name='want_detail'),
]