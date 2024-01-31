from django import forms
from .models import WorkExperience,  Education, Skill, Achievement, Profile

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['title', 'company', 'start_date', 'end_date', 'description']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'university', 'graduation_date', 'cgpa']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['title']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'title', 'contact_number_1', 'contact_number_2', 'email', 'github_url', 'overview']



