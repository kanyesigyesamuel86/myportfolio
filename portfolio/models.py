from django.db import models
from django.contrib.auth.models import User
from django import forms


class WorkExperience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"


class Education(models.Model):
    degree = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    graduation_date = models.DateField()
    cgpa = models.FloatField()

    def __str__(self):
        return f"{self.degree} at {self.university}"

class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=255)
    description =models.TextField()
    link = models.URLField()

class Hobby(models.Model):
    title = models.CharField(max_length=50)

    
    

class Profile(models.Model):
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    contact_number_1 = models.CharField(max_length=20)
    contact_number_2 = models.CharField(max_length=20)
    email = models.EmailField()
    github_url = models.URLField()
    overview = models.TextField()

    work_experiences = models.ManyToManyField(WorkExperience)
    skills = models.ManyToManyField(Skill)
    achievements = models.ManyToManyField(Achievement)
    education = models.ManyToManyField(Education)
    project = models.ManyToManyField(Project)
    hobby = models.ManyToManyField(Hobby)
    

    def __str__(self):
        return self.full_name