from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import generics
from .serializers import IngredientSerializer, BlogSerializer, CommentSerializer
from .models import Ingredient, Blog, Comment
from rest_framework import viewsets
from .forms import BlogForm
# Create your views here.


class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


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


# def test_view(request, *args, **kwargs):
#     print(args, kwargs)
#     print(request.user)
#     return HttpResponse("<h1>wtf</h1>")

# @login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()

            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'dandelion/blog_form.html', {'form': form})
