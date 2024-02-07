from django import forms
from .models import WorkExperience,  Education, Skill, Achievement, Profile, Project, Hobby, Contact

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['position', 'company', 'start_date', 'end_date', 'work_done']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['program', 'school_or_university', 'grade', 'year_started', 'year_ended']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['name', 'url']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'area_of_study', 'contact_number_1', 'contact_number_2', 'email', 'github_url', 'summary']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link']


class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['title']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'