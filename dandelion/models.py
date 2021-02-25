from django.db import models
from users.models import User

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=300)
    description = models.TextField(null=False, blank=False)
    key_benefits = models.TextField()
    usage = models.TextField()
    taste = models.TextField()
    caution = models.TextField()
    photo_url = models.TextField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    written_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author')
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name='ingredient')
    title = models.CharField(max_length=100)
    byline = models.CharField(max_length=300)
    body = models.TextField()
    photo_url = models.TextField(null=True, blank=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='blog'
    )
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.author
