from django.db import models
from django.contrib.auth.models import User
from django import forms


class WorkExperience(models.Model):
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    work_done = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"


class Education(models.Model):
    program = models.CharField(max_length=255)
    school_or_university = models.CharField(max_length=255)
    grade = models.CharField(max_length = 20)
    year_started = models.IntegerField(null = True, blank = True)
    year_ended= models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.program} at {self.school_or_university}"

class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(null = True, blank = True)

    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=255)
    description =models.TextField()
    link = models.URLField()
    def save(self, *args, **kwargs):
        outlines = self.description.split(". ")
        self.description = "\n".join(outlines)
        super().save(*args, **kwargs)

class Hobby(models.Model):
    title = models.CharField(max_length=50)

    
class Profile(models.Model):
    full_name = models.CharField(max_length=255)
    area_of_study = models.CharField(max_length=255)
    contact_number_1 = models.CharField(max_length=20)
    contact_number_2 = models.CharField(max_length=20)
    email = models.EmailField()
    github_url = models.URLField()
    summary = models.TextField()

    work_experiences = models.ManyToManyField(WorkExperience)
    skills = models.ManyToManyField(Skill)
    achievements = models.ManyToManyField(Achievement)
    education = models.ManyToManyField(Education)
    project = models.ManyToManyField(Project)
    hobby = models.ManyToManyField(Hobby)
    
    def __str__(self):
        return self.full_name

class Contact(models.Model):
    email_field = models.EmailField()
    tel = models.TextField(max_length =200)
    message_field= models.TextField(max_length =200)