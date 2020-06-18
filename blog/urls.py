from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="post_list"),
    path('givelist/',  views.GiveListView.as_view(), name='give_list'),
    path('wantlist/', views.WantListView.as_view(), name='want_list'),
    path('givenew/', views.GiveCreateView.as_view(), name='give_new'),
    path('wantnew/', views.WantCreateView.as_view(), name='want_new'),
    path('profilelist/', views.ProfileListView.as_view(), name='profile_list'),
    path('profilenew/', views.ProfileCreateView.as_view(), name='profile_new'),
    path('give<int:pk>/',views.GiveDetailView.as_view(), name='give_detail'),
    path('want<int:pk>/', views.WantDetailView.as_view(), name='want_detail'),
    path('profile<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('give/<int:pk>/comment/', views.add_comment_to_give, name='add_comment_to_give'),
    path('give/comment/<int:pk>/remove/', views.give_comment_remove, name='give_comment_remove'),
    path('want/<int:pk>/comment/', views.add_comment_to_want, name='add_comment_to_want'),
    path('profile/<int:pk>/comment/', views.add_comment_to_profile, name='add_comment_to_profile'),
    path('want/comment/<int:pk>/remove/', views.want_comment_remove, name='want_comment_remove'),
    path('comment/<int:pk>/remove/', views.give_comment_remove, name='give_comment_remove'),
    path('profile/comment/<int:pk>/remove/', views.profile_comment_remove, name='profile_comment_remove'),
    path('give-delete/<int:pk>/', views.GiveDeleteView.as_view(), name="give_delete"),
    path('give-update/<int:pk>/', views.GiveUpdateView.as_view(), name="give_update"),
]