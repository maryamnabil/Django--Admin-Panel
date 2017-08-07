# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SignUp (models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Name =models.CharField (max_length=120, blank=False , null=True)
    Email=models.EmailField ()
    phone =models.CharField (max_length=120, blank=False , null=True)
    Age =models.CharField (max_length=3, blank=True , null=True)
    gender = models.CharField(max_length=1, blank=True ,choices=GENDER_CHOICES)
    Comments =models.TextField(blank=True,db_column="clean")

    def __unicode__(self):
     return self.Email
     return  self.Name
     return  self.Phone
     return  self.Age
     return  self.gender
     return  self.comments