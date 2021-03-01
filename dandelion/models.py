from django.db import models
from users.models import User

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=300)
    photo_url = models.TextField()
    key_benefits = models.TextField()
    taste = models.TextField()
    usage = models.TextField()
    description = models.TextField(null=False, blank=False)
    caution = models.TextField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    written_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_blogs', null=True, blank=True)
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name='blogs', null=True, blank=True)
    title = models.CharField(max_length=100)
    byline = models.CharField(max_length=300)
    photo_url = models.TextField(null=True, blank=True)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comments', null=True, blank=True)
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments', null=True, blank=True
    )
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.body
