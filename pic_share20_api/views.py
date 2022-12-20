from rest_framework import generics
from django.shortcuts import render
from pic_share20_api.models import Follow_users, Posts, Users
from pic_share20_api.serializers import Follower_usersSerializer, PostsSerializer, UsersSerializer
from rest_framework import viewsets
from rest_framework_api_key.permissions import HasAPIKey 
from rest_framework.permissions import IsAuthenticated

class PostsViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = Posts.objects.order_by('created_at').reverse()
    serializer_class = PostsSerializer

    def perform_create(self, serializer, **kwarhgs):
        serializer.save()


class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UserFollowingViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = Follower_usersSerializer
    queryset = Follow_users.objects.all()

    def perform_create(self, serializer, **kwarhgs):
        serializer.save()
