from django.urls import path
from . import views

app_name = 'blog'  # Add the app name (if not already present)

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/create/', views.PostCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
]
