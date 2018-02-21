from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    bio= models.TextField()
    born_at = models.DateField()
    died_at = models.DateField()
    author_pic = models.ImageField(default = '/home/linamasoud/Documents/user.png')
    user_id = models.ManyToManyField(User,related_name="User_Author")


