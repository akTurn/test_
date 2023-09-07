from django.db import models


# Create your models here.
class Office(models.Model):
    officeCode = models.CharField(max_length=10, primary_key=True)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    addressLine1 = models.CharField(max_length=50)
    addressLine2 = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50)
    postalCode = models.CharField(max_length=15)
    territory = models.CharField(max_length=10)

    class Meta:
        db_table = 'venue'
        #managed=False
    #def __str__(self):
        #return self.officeCode