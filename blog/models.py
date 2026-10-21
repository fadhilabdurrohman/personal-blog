import uuid
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    CREATED_BY_CHOICES = [
        ('author', 'Author'),
        ('guest', 'Guest'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=20, choices=CREATED_BY_CHOICES, default='author')
    content = CKEditor5Field(config_name='default')
    thumbnail = models.ImageField(upload_to='media/img/', blank=True, null=True)
    tag = models.ManyToManyField(Tag, related_name="posts", blank=True)

    def __str__(self):
        return self.title
