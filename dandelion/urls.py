from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls import url

urlpatterns = [
    path("roots/", views.IngredientList.as_view(), name="ingredient_list"),
    path("roots/<int:pk>", views.IngredientDetail.as_view(),
         name="ingredient_detail"),
    #     path("roots/search/", views.IngredientSearch.as_view(),
    #          name="ingredient_search"),
    path("blogs/", views.BlogList.as_view(), name="blog_list"),
    path("blogs/<int:pk>",
         views.BlogDetail.as_view(), name="blog_detail"),
    path("comments/", views.CommentList.as_view(), name="comment_list"),
    path("comments/<int:pk>", views.CommentDetail.as_view(), name="comment_detail"),
    url(r'^blogs/new$', views.blog_create, name='blog_create'),
    url(r'^comments/new$', views.comment_create, name='comment_create'),

]
