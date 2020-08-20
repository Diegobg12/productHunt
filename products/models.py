from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length = 255)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail',args=([str(self.id)]))

class Product(models.Model):
    title = models.CharField(max_length=20)
    pub_date =  models.DateTimeField()
    body =  models.TextField()
    author = models.CharField(max_length=20, null =True, blank = True)
    url =  models.TextField()
    image = models.ImageField(upload_to='images/')
    votes_total= models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,null=True, default='1')
    
  

    def summary(self):
        return self.body[:100]

    def pub_date_short(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title

