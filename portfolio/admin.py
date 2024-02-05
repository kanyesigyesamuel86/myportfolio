from django.contrib import admin
from .models import Profile, WorkExperience, Education, Skill, Achievement, Project, Hobby

# Register your models here.
admin.site.register(Profile)
admin.site.register(WorkExperience)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Achievement)
admin.site.register(Education)
admin.site.register(Hobby)