from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path("roots/", views.IngredientList.as_view(), name="ingredient_list"),
    path("roots/<int:pk>", views.IngredientDetail.as_view(),
         name="ingredient_detail"),

]
