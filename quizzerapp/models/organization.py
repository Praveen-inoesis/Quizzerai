# quizzerapp/models/organization.py

from django.db import models
from django.core.validators import FileExtensionValidator, RegexValidator   

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(
        max_length=6,
        validators=[RegexValidator(regex=r'^\d{6}$', message="Postal code must be exactly 6 digits.")]
    )
    phone_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{10}$', message="Phone number must be exactly 10 digits.")]
    )

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country}, {self.postal_code}"

class Organization(models.Model):
    organization_name = models.CharField(max_length=255, unique=True)
    organization_id = models.AutoField(primary_key=True, unique=True)
    domain_name = models.CharField(max_length=255, unique=True)
    admin_email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    disable = models.BooleanField(default=False)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='organization', null=True, blank=True)

    def __str__(self):
        return self.organization_name


