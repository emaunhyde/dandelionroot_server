from django.contrib import admin
from .models import Ingredient, Blog, Comment
# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Blog)
admin.site.register(Comment)
