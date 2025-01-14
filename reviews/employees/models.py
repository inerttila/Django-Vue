from django.db import models

# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=100, null=True)
    dep = models.TextField(max_length=30, null=True)
    birthdate = models.CharField(max_length=30, null=True)
    salary = models.TextField(max_length=30, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.fullname


class Review(models.Model):
    SHOP_CHOICES = [
        ('Shop 1', 'Shop 1'),
        ('Shop 2', 'Shop 2'),
    ]

    userName = models.CharField(max_length=100, null=True)
    thumbsUppCount = models.IntegerField(null=True)
    thumbsDownCount = models.IntegerField(null=True)
    review = models.TextField(max_length=100, null=True)
    shop = models.CharField(
        max_length=20, 
        choices=SHOP_CHOICES,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.userName
