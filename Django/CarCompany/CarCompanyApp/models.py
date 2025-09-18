from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
# Cars available for buying
class Car(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="cars/")   # requires MEDIA settings

    def __str__(self):
        return self.name
class Contact(models.Model):
    First_Name = models.CharField(max_length=122)
    Last_Name = models.CharField(max_length=122)
    Email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)  
    message = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.Email
    
class Sell(models.Model):
    owner_name = models.CharField(max_length=122)
    contact_no = models.CharField(max_length=14)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=150)  
    car_name = models.CharField(max_length=122)
    model = models.CharField(max_length=14)
    year = models.CharField(max_length=254)
    price = models.CharField(max_length=20)  
    condition = models.CharField(max_length=20, choices=[('Well','Well'),('Average','Average'),('Not Good','Not Good')])
    image = models.ImageField(upload_to="car_images/", blank=True, null=True)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.owner_name
    
class CarService(models.Model):
    SERVICE_CHOICES = [
        ("General Service", "General Service"),
        ("Engine Check", "Engine Check"),
        ("Oil Change", "Oil Change"),
        ("Tyre Replacement", "Tyre Replacement"),
        ("AC Repair", "AC Repair"),
        ("Other", "Other"),
    ]
    owner_name = models.CharField(max_length=122)
    contact_no = models.CharField(max_length=14)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=150)  
    car_name = models.CharField(max_length=122)
    model = models.CharField(max_length=14)
    year = models.CharField(max_length=254)
    services = models.TextField()

    def __str__(self):
        return self.owner_name


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=200)
    car_image = models.ImageField(upload_to='wishlist/', blank=True, null=True)
    price = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.car_name}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=200)
    car_image = models.ImageField(upload_to='cars/', blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.car_name}"