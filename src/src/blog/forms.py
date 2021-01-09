from django import forms
from django.db.models import fields
from .models import Post, Comment, Category


class PostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Post.OPTIONS)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label="Select")

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'image',
            'category',
            'status',
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
