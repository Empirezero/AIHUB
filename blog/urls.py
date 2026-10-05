from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('post/new/', views.post_create, name='post-create'),
    path('post/<slug:slug>/', views.post_detail, name='post-detail'),
    path('post/<slug:slug>/edit/', views.post_update, name='post-update'),
    path('post/<slug:slug>/delete/', views.post_delete, name='post-delete'),
    path('api/', include(router.urls)),
]