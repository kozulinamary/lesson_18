from django.urls import path
from .views import post_views, PostListView

urlpatterns = [
    path('all_posts_func/', post_views, name='all_posts_func'),
    path('post/<str:post_id>/', post_views, name='single_post'),
    path('all_posts_class/', PostListView.as_view(), name='all_posts_class'),
]