from django.db import models

class CompanyDetails(models.Model):
    banner_img = models.ImageField(upload_to='company_banners/')
    banner_heading = models.CharField(max_length=255)
    banner_paragraph = models.TextField()
    vision_heading = models.CharField(max_length=255)
    vision_paragraph = models.TextField()
    mission_heading = models.CharField(max_length=255)
    mission_paragraph = models.TextField()
    happy_clients = models.PositiveIntegerField()
    awards_won = models.PositiveIntegerField()
    projects = models.PositiveIntegerField()
    momentum = models.TextField()
    recognitions = models.TextField()
    works_done = models.ImageField(upload_to='company_works/')
    compliments = models.TextField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    x_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
