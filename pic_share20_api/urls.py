from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('follow_users', views.UserFollowingViewSet)
router.register('posts', views.PostsViewSet)
router.register('users', views.UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
