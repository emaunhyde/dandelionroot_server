from rest_framework import serializers
from .models import Ingredient, Blog, Comment
from users.models import User
from users.serializers import UserCreateSerializer


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'body', 'created_at',  'author')


class BlogSerializer(serializers.HyperlinkedModelSerializer):
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
        fields = ('id', 'ingredient', 'title',
                  'byline', 'body', 'photo_url', 'created_at', 'comments', 'written_by')


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    blogs = BlogSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'scientific_name', 'description',
                  'key_benefits', 'usage', 'taste', 'caution', 'photo_url', 'blogs')
