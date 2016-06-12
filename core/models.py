from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator

class UserProfile(AbstractUser):
    address = models.CharField(max_length=100)
    address_2 = models.CharField(blank=True, max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = CountryField()

class UserFinancialSettings(models.Model):
    owners = UserProfile.objects.filter(
        models.Q(username='john')|
        models.Q(username='bill')
    )
    OWNERS = (
        zip([owner.first_name for owner in owners],
            [owner.first_name for owner in owners])
    )
    OWNERS.insert(0, ('','House Account'))
    METHODS = (
        ('Paypal', 'Paypal'),
        ('Paxum', 'Paxum'),
        ('Skrill', 'Skrill'),
        ('Wire','Wire'),
        ('Check', 'Check'),
        ('ADE_Ban', 'ADE Ban')
    )
    TERMS = (
        ('Standard', 'Standard'),
        ('Net_1_Day', 'Net 1 Day'),
    )
    user = models.OneToOneField(UserProfile, null=True, blank=True)
    publisher_owner = models.CharField(max_length=50, choices=OWNERS, blank=False, default=0)
    payment_method = models.CharField(max_length=50, choices=METHODS)
    payment_email = models.EmailField(max_length=50)
    payment_terms = models.CharField(max_length=50, choices=TERMS)
    payment_minimum = models.DecimalField(decimal_places=2,
        max_digits=5, default=Decimal('0.00'), validators=[MinValueValidator(0.00)])
