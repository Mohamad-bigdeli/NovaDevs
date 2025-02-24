from django.db import models

# Create your models here.

class Member(models.Model):
    image = models.ImageField()
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    age = models.PositiveIntegerField()
    marital_status = models.CharField(max_length=225)
    education = models.CharField(max_length=225)
    residence = models.CharField(max_length=225)
    military_status = models.CharField(max_length=225)
    description = models.TextField()
    skills = models.TextField()
    resume = models.FileField(upload_to="resumes/")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Service(models.Model):
    title  = models.CharField(max_length=225)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
