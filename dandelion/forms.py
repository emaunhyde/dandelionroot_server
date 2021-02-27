from django import forms
from .models import Blog, Comment


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'byline', 'photo_url',
                  'body', 'ingredient', 'written_by')
