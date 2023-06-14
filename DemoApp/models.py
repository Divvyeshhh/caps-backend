from django.db import models

# Create your models here.
class Caps(models.Model):
    complaint = models.IntegerField(null = True, blank = True, default = None)
    complaint_type = models.CharField(max_length=100, null = True, blank = True, default = None)
    complaint_place = models.CharField(max_length=100, null = True, blank = True, default = None)
    informant_type = models.CharField(max_length=100, null = True, blank = True, default = None)    
    def __str__(self):
        return self.complaint_type


class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Business(models.Model):
    city = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Package(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name