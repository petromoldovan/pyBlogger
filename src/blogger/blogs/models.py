from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
import uuid

# Create your models here.
class Post(models.Model):
    uuid = models.UUIDField(default=uuid.uuid5(uuid.NAMESPACE_URL, 'blogs'), editable=False, unique=True)
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    tab_name = models.CharField(max_length=255, default="this is default tab name")
    author = models.ForeignKey(User, on_delete=models.CASCADE) #CASCADE if we delete user, his posts are deleted
    body = models.TextField()

    def __str__(self):
        # name in the list
        return self.title + ' | by: ' + str(self.author)

    def get_absolute_url(self):
        # where to redirect when post is created
        return reverse('article-details', args=(str(self.id)))
        #return reverse('home')