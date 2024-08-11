"""
URL configuration for social_network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts import views
from posts.views import LikeViewSet, CommentViewSet, AddLikeView

from rest_framework.routers import DefaultRouter
 
router = DefaultRouter()
router.register('likes', LikeViewSet, basename='likes')
router.register('comments', CommentViewSet, basename='posts') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.PostListView.as_view(), name='PostListView'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='PostDetailView'),
    path('posts/<int:post_id>/like/', AddLikeView.as_view(), name='add_like'),
] + router.urls