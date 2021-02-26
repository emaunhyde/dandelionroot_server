from rest_framework import serializers
from .models import Ingredient, Blog, Comment
from users.models import User


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    blogs = serializers.HyperlinkedRelatedField(
        view_name='blog_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'scientific_name', 'description',
                  'key_benefits', 'usage', 'taste', 'caution', 'photo_url', 'blogs')


class BlogSerializer(serializers.HyperlinkedModelSerializer):

    ingredient = serializers.HyperlinkedRelatedField(
        view_name='ingredient_detail',
        many=False,
        read_only=True
    )

    class Meta:
        model = Blog
        fields = ('id', 'ingredient', 'title',
                  'byline', 'body', 'photo_url', 'created_at', 'comments')

    comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Blog
        fields = ('id', 'ingredient', 'title',
                  'byline', 'body', 'photo_url', 'created_at', 'comments')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    blogs = serializers.HyperlinkedRelatedField(
        view_name='blog_detail',
        many=False,
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'body', 'created_at', 'blogs')
