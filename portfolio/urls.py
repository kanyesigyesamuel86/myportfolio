from django.urls import path
from .views import home, about_me, profile, profile_1, add_work_experience, update_work_experience, update_profile, add_education, update_education, add_skill, add_achievement, add_project, add_hobby, custom_logout, DeleteExperienceView, DeleteAchievementView, DeleteEducationView, DeleteHobbyView, DeleteProjectView, DeleteSkillView, login_with_otp, verify_otp, contact
from django.views.generic import TemplateView


urlpatterns = [
    path('login/', login_with_otp, name = 'login'),
    path('logout/', custom_logout, name='logout'),
    path('', home, name = 'home'),
    path('home/', home, name = 'home'),
    path('about_me', about_me, name= 'about_me'),
    path('profile/', profile, name = 'profile'),
    path('profile_1/', profile_1, name = 'profile_1'),
    path('update_profile/', update_profile, name='update_profile'),
    path('add_work_experience/', add_work_experience, name='add_work_experience'),
    path('update_work_experience/<int:pk>/', update_work_experience, name='update_work_experience'),
    path('add_education/', add_education, name='add_education'),
    path('update_education/<int:pk>/', update_education, name='update_education'),
    path('add_skill', add_skill, name = 'add_skill'),
    path('add_achievement/', add_achievement, name= 'add_achievement'),
    path('add_project/', add_project, name = 'add_project'),
    path('add_hobby/', add_hobby, name = 'add_hobby'),
    path('delete_experience/<int:pk>/', DeleteExperienceView.as_view(), name='delete_experience'),
    path('delete_achievement/<int:pk>/', DeleteAchievementView.as_view(), name='delete_achievement'),
    path('delete_education/<int:pk>/', DeleteEducationView.as_view(), name='delete_education'),
    path('delete_project/<int:pk>/', DeleteProjectView.as_view(), name='delete_project'),
    path('delete_hobby/<int:pk>/', DeleteHobbyView.as_view(), name='delete_hobby'),
    path('delete_skill/<int:pk>/', DeleteSkillView.as_view(), name='delete_skill'),
    path('verify_otp/', verify_otp, name = 'verify_otp'),
    path('contact/', contact, name = 'contact'),
    path('success/', TemplateView.as_view(template_name='success_page.html'), name='success'),
  

]
