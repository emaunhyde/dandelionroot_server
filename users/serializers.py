from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models
from dandelion.serializers import BlogSerializer, CommentSerializer


class UserCreateSerializer(UserCreateSerializer):

    user_blogs = BlogSerializer(
        many=True,
        read_only=True
    )

    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'username', 'password',
                  'photo_url', 'bio', 'user_blogs')
