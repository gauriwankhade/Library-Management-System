from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Member(AbstractUser):
    username        = models.CharField(max_length=30,unique=True)
    password        = models.CharField(max_length=100)
    email           = models.EmailField(unique=True)
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    member_type     = models.CharField(default='student',max_length=30)

    class Meta:
        verbose_name = _("Member")
        ordering = ['last_name']


    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['name']


class Author(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    country = CountryField(blank_label='(select country)')

   
    def __str__(self):
        return self.name + ' ' + self.surname + ' from ' + self.country.name

    class Meta:
        ordering = ['surname']

class Book(models.Model):
    choices = (('Available','Available'),('NA','Not available'))
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    categories = models.ForeignKey(Category,on_delete=models.CASCADE)
    status = models.CharField(max_length=55,choices=choices,default='Available')
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class IssueRequest(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    book    = models.ForeignKey(Book,on_delete=models.CASCADE)
    date_added  = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

  






