from itertools import product
from django.db import models

class People(models.Model):
  first_name = models.CharField(max_length=255, default='')
  last_name = models.CharField(max_length=255, default='')
  email = models.EmailField(default='')
  contact = models.CharField(max_length=255, default='')
  
  def __str__(self):
        return self.first_name
 
class Doctor(models.Model):
  blood_pressure = models.CharField(max_length=255, default='')
  sugar_level = models.CharField(max_length=255, default='')
  disabilities = models.CharField(max_length=255, default='')
  person = models.ForeignKey(People, on_delete=models.CASCADE, default='')
  
  def __str__(self):
        return self.doctor_name
      
class Bio(models.Model):
  hobbies = models.CharField(max_length=255, default='')
  date_of_birth = models.DateField(default='')
  biggest_achievement = models.CharField(max_length=200, default='')
  people = models.ForeignKey(People, on_delete=models.CASCADE, default='')
  
  def __str__(self):
        return self.hobbies
      
class Address(models.Model):
  street_number_and_name = models.CharField(max_length=220, default='')
  user = models.OneToOneField(People, on_delete=models.CASCADE, default='') 
  
  def __str__(self):
      return self.street_number_and_name
    
class Product(models.Model):
  product_name = models.CharField(max_length=220)  
  product_price = models.CharField(max_length=220)  
  product_category = models.CharField(max_length=220)  
  
  def __str__(self):
        return self.product_name
      