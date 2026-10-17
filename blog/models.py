from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    content = CKEditor5Field(config_name='default')
    thumbnail = models.ImageField(upload_to='media/img/')
    tag = models.ManyToManyField(Tag, related_name="posts", blank=True)

    def __str__(self):
        return self.title
