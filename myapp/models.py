from django.db import models
from django.contrib.auth.models import User

class Collections(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.phone}"
    
class Car(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/')
    
    def __str__(self):
        return self.name 

class Order(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),  
    ]
    customer = models.ForeignKey(Collections, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='confirmed')


    def __str__(self):
        return f"{self.car_name} - {self.customer.name} - {self.status}"
