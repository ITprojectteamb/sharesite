from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="post_list"),
    path('givelist/',  views.GiveListView.as_view(), name='give_list'),
    path('wantlist/', views.WantListView.as_view(), name='want_list'),
    path('givenew/', views.GiveCreateView.as_view(), name='give_new'),
    path('wantnew/', views.want_new, name='want_new'),
    path('profilenew/', views.profile_new, name='profile_new'),
    path('give<int:pk>/',views.GiveDetailView.as_view(), name='give_detail'),
    path('want<int:pk>/', views.want_detail, name='want_detail'),
    path('mypage/', views.mypage, name='mypage'),
    path('give/<int:pk>/comment/', views.add_comment_to_give, name='add_comment_to_give'),
    path('comment/<int:pk>/remove/', views.give_comment_remove, name='give_comment_remove'),
    path('give-delete/<int:pk>/', views.GiveDeleteView.as_view(), name="give_delete"),
    path('give-update/<int:pk>/', views.GiveUpdateView.as_view(), name="give_update"),
]