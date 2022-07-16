from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
class Store(models.Model):
    store_name = models.CharField(max_length=20)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='user',verbose_name='Owner')
    def __str__(self):
        return self.store_name
class Book(models.Model):
    Book_id = models.CharField(max_length=100)
    no_copis = models.IntegerField(null=True)
    store = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='store')
    def __str__(self):
        return self.Book_id

# Create your models here.
