from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
import uuid
from ckeditor.fields import RichTextField

class Category(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        # name in the list
        return self.name

    def get_absolute_url(self):
        # where to redirect when post is created
        return reverse('post-list')

# Create your models here.
class Post(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    tab_name = models.CharField(max_length=255, default="this is default tab name")
    author = models.ForeignKey(User, on_delete=models.CASCADE) #CASCADE if we delete user, his posts are deleted
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='user_post_likes')
    snippet = models.TextField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def get_total_likes(self):
        return self.likes.count()

    def __str__(self):
        # name in the list
        return self.title + ' | by: ' + str(self.author)

    def get_absolute_url(self):
        # where to redirect when post is created
        #return reverse('article-details', args=(str(self.id)))
        return reverse('post-list')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars/')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        # name in the list
        return str(self.user)

    def get_absolute_url(self):
        # where to redirect when creation is done
        return reverse('post-list')

class Comment(models.Model):
    created = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        # name in the list
        return self.post.title + '| by ' + self.name