from django.forms import ModelForm, TextInput, Select, Textarea
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'created_by', 'content', 'thumbnail', 'tag']
        labels = {
            'title': 'Title',
            'created_by': 'Created by',
            'content': 'Content',
            'thumbnail': 'Thumbnail',
            'tag': 'Tag',
        }
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': '...',
                    'max_length': 255,
                }
            ),
            'created_by': Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'content': CKEditor5Widget(
                config_name='default',
            ),
        }
