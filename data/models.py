from django.db import models


# Create your models here.
class Mastersheet(models.Model):
    companiesname = models.CharField(max_length=40, blank=False)
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    Title = models.CharField(max_length=40, blank=False)
    Email = models.CharField(max_length=40, blank=False)
    url = models.CharField(max_length=40, blank=False)
    #mobile_number = models.CharField(max_length=10, blank=True)
    #description = models.TextField(max_length=255, blank=False)
    #location = models.TextField(max_length=255, blank=False)
    #date = models.DateField('%m/%d/%Y')
    #created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    #updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')

class Count(models.Model):
    companiesname = models.CharField(max_length=40, blank=False)
    count = models.CharField(max_length=40, blank=False)
    #document = models.CharField(max_length=255, )
    #uploaded_at = models.DateTimeField(auto_now_add=True)

class Retail(models.Model):
    companiesname = models.CharField(max_length=40, blank=False)
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    Title = models.CharField(max_length=40, blank=False)
    Email = models.CharField(max_length=40, blank=False)
    url = models.CharField(max_length=40, blank=False)

class Retail_Count(models.Model):
    companiesname = models.CharField(max_length=40, blank=False)
    count = models.CharField(max_length=40, blank=False)
    #document = models.CharField(max_length=255, )
    #uploaded_at = models.DateTimeField(auto_now_add=True)


class Financial(models.Model):
    companiesname = models.CharField(max_length=40, blank=False)
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    Title = models.CharField(max_length=40, blank=False)
    Email = models.CharField(max_length=40, blank=False)
    url = models.CharField(max_length=40, blank=False)

class Financial_Count(models.Model):
    companiesname = models.CharField(max_length=40, blank=False)
    count = models.CharField(max_length=40, blank=False)
    #document = models.CharField(max_length=255, )
    #uploaded_at = models.DateTimeField(auto_now_add=True)


class Leadfedder(models.Model):
    companiesname = models.CharField(max_length=40, blank=False)
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    Title = models.CharField(max_length=40, blank=False)
    Email = models.CharField(max_length=40, blank=False)
    url = models.CharField(max_length=40, blank=False)

class Leadfedder_Count(models.Model):
    companiesname = models.CharField(max_length=40, blank=False)
    count = models.CharField(max_length=40, blank=False)
    #document = models.CharField(max_length=255, )
    #uploaded_at = models.DateTimeField(auto_now_add=True)




def __str__(self):
		return self.last_name