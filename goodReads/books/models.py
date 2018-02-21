from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    desciption= models.TextField()
    published_at = models.DateField()
    book_pic = models.ImageField(default = '/home/linamasoud/Documents/book.png')
    wish_list = models.ManyToManyField(User,related_name="User_Book_Wishlist")
    read = models.ManyToManyField(User,related_name="User_Book_read")


class rateBook(models.Model):

    rate = models.IntegerField()
    user_id = models.ForeignKey(User)
    book_id = models.ForeignKey(Book)

