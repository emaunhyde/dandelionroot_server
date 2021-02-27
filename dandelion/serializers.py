from rest_framework import serializers
from .models import Ingredient, Blog, Comment
from users.models import User
from users.serializers import UserCreateSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'body', 'created_at',  'author')


class BlogSerializer(serializers.ModelSerializer):

    written_by = UserCreateSerializer(
        many=False,
        read_only=True
    )

    ingredient = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    comments = CommentSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Blog
        fields = ('id', 'title', 'ingredient', 'written_by',
                  'byline', 'body', 'photo_url', 'created_at', 'comments')


class IngredientSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'scientific_name', 'description',
                  'key_benefits', 'usage', 'taste', 'caution', 'photo_url', 'blogs')
