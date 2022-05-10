from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    amount = models.IntegerField()
    tenture = models.IntegerField(null=True, blank=True)
    DEPARTMENTS = (
        ('', 'Select'),
        ('IT employee', 'Goverment staff'),
        ('Business', 'IT employee'),
        ('Startup', 'Business'),
    )
    occupation = models.CharField(max_length=100, null=True, blank=True, choices=DEPARTMENTS)
    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDERS, null=True, default=None)
    interest = models.IntegerField()
    Income = (
        ('<500000', '<500000'),
        ('500000-1000000', '500000-1000000'),
        ('>1000000', '>1000000'),
    )
    income = MultiSelectField(max_length=150, null=True, blank=True, choices=Income)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
