from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import generics, viewsets
from .serializers import IngredientSerializer, BlogSerializer, CommentSerializer
from .models import Ingredient, Blog, Comment
# from django_filters import rest_framework as filters
from .forms import BlogForm, CommentForm
# Create your views here.


class IngredientList(generics.ListCreateAPIView):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# class IngredientSearch(generics.ListAPIView):
#     query_set = Ingredient.objects.all()
#     serializer = IngredientSerializer
#     filter_backends = (filters.DjangoFilterBackend)
#     filterset_fields = ('description', 'key_benefits')


def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()

            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'dandelion/blog_form.html', {'form': form})


def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()

            return redirect('blog_list')
    else:
        form = CommentForm()
    return render(request, 'dandelion/comment_form.html', {'form': form})
