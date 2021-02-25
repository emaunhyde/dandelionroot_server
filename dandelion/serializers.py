from rest_framework import serializers
from .models import Ingredient, Blog, Comment


class IngredientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'scientific_name', 'description',
                  'key_benefits', 'usage', 'taste', 'caution', 'photo_url')


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    ingredient = serializers.HyperlinkedRelatedField(
        view_name='ingredient_detail',
        many=False,
        read_only=True
    )

    class Meta:
        model = Blog
        fields = ('id', 'ingredient', 'title', 'written_by',
                  'byline', 'body', 'photo_url', 'created_at')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    blog = serializers.HyperlinkedRelatedField(
        view_name='blog_detail',
        many='False',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'blog', 'body', 'created_at')
