from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.conf import settings

class Category(models.Model):
  name = models.CharField(max_length=255)
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('home')


class Post(models.Model):
  title = models.CharField(max_length=255)
  title_tag = models.CharField(max_length=255)
  header_image = models.ImageField(null=True, blank=True, upload_to='images/')
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  category = models.CharField(max_length=255, default='general tips')
  snippet = models.CharField(max_length=255, default='')
  post_date = models.DateField(auto_now_add=True)
  body = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.title + ' | '+ str(self.author.first_name)

  def get_absolute_url(self):
    return reverse('home')
