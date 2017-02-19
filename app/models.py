﻿"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
#from recommendationservice import RecommendationService

# Create your models here.

from django.core.exceptions import ValidationError
import config
def validate_true(value):
    if value is not True:
        raise ValidationError("This value is required to be true.")

def validate_not_empty(value):
    if not value:
        raise ValidationError("Field must not be blank.")

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Address Fields
    address = models.CharField(max_length=200, validators=[validate_not_empty])
    city = models.CharField(max_length=50, validators=[validate_not_empty])
    state = models.CharField(max_length=2, validators=[validate_not_empty])
    zip_code = models.CharField(max_length=10, validators=[validate_not_empty]) # 12345-1234.  Will this be good for Canada?

    # Other fields here
    url = models.URLField("Website", blank=True)

# create the user profile on post save of user accounts
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=512)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_link = models.CharField(max_length=100)

    @property
    def recommended_items(self):
        # Use data marketplace service to get recommendations
        rs = RecommendationService(config.azure_datamarket_email, config.azure_datamarket_access_key)
        recommendations = rs.get_recommendation(config.model_id, [ str(self.id) ])
        recommend_products = [ Product.objects.get(id=int(r.id)) for r in recommendations ]
        return recommend_products
