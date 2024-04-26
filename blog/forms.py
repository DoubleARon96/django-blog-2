from .models import Comment
from django import forms

"""
Form class for users to comment on a post 
"""

class CommentForm(forms.ModelForm):

    """
    Specify the django model and order of the fields
    """

    class Meta:
        model = Comment
        fields = ('body',)