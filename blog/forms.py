from django import forms
from django.forms import HiddenInput
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {'body': forms.Textarea(attrs={'cols': 20, 'rows': 5})}