from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
# class DealType(models.Model):
#     name = models.CharField(max_length=150, null=False, blank=False)

class Deal(models.Model):
    #Deail_id = models.AutoField()
    dealId = models.CharField(max_length=150, primary_key=True, null=False, blank=False, default=1)
    dealname = models.CharField(max_length=150, null=False, blank=False)
    dealstage = models.CharField(max_length=150, null=True, blank=True)
    closedate = models.DateField(null=True, blank=True, default=datetime.now)
    amount = models.DecimalField(null=True, max_digits=20, decimal_places=3)
    dealtype = models.CharField(max_length=150, null=True, blank=True)

#This is an extension of the User model that django provided. We need to add more detail to our user, 
# in this case we are just adding the token prop to persist it
class IntegrationUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=150, null=False, blank=False)
    token_expiration = models.DateField(null=False, blank=False)



