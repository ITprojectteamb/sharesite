from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="post_list"),
    path('givelist/',  views.GiveListView.as_view(), name='give_list'),
    path('wantlist/', views.WantListView.as_view(), name='want_list'),
    path('givenew/', views.give_new, name='give_new'),
    path('wantnew/', views.want_new, name='want_new'),
    path('profilenew/', views.profile_new, name='profile_new'),
    path('give<int:pk>/', views.give_detail, name='give_detail'),
    path('want<int:pk>/', views.want_detail, name='want_detail'),

##################################################################
#ここから先追加箇所＃
##################################################################

    path('mypage/', views.mypage, name='mypage'),
    path('give/<int:pk>/edit/', views.give_edit, name='give_edit'),
    path('give/remove/<int:pk>/', views.give_remove, name='give_remove'),
]