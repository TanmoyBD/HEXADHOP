from django.db import models
from accounts.models import CustomUser

class Seller(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='seller_profile', null=True, blank=True)

    name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='photos/seller_profile_picture', null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=False)
    is_seller = models.BooleanField(default=False)
    company_name = models.CharField(max_length=255)
    website = models.URLField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    confirmation_code=models.IntegerField(max_length=6,null=True)

    def __str__(self):
        return self.name  # Replace with a suitable field to represent the Seller

    class Meta:
        verbose_name_plural = 'Sellers'
        
        

