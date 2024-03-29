from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Profile, WorkExperience, Education, Skill, Achievement, Project, Hobby
from .forms import WorkExperienceForm, ProfileForm, EducationForm, SkillForm, AchievementForm, ProjectForm, HobbyForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.views import View
from django.http import HttpResponseForbidden, HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
import datetime
from django.contrib.admin.views.decorators import staff_member_required

def custom_logout(request):
    logout(request)
    return redirect('home') 

def home(request):
    return render(request, 'home.html')

def about_me(request):
    return render(request, 'about_me.html')

@login_required
def profile_1(request):
    my_profile, created = Profile.objects.get_or_create(id=1)
    # Pass the profile instance to the template
    context = {'profile': my_profile}
    return render(request, 'profile_1.html', context)


def profile(request):
    my_profile, created = Profile.objects.get_or_create(id=1)
    # Pass the profile instance to the template
    context = {'profile': my_profile}
    return render(request, 'profile.html', context)

@login_required
def update_profile(request):
    profile, created = Profile.objects.get_or_create(id=1)  # Assuming the profile has id=1

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_1')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'update_profile.html', {'form': form})


@login_required
def add_work_experience(request):
    profile, created = Profile.objects.get_or_create(id=1)

    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            work_experience_instance = form.save()
            profile.work_experiences.add(work_experience_instance)
            messages.success(request, 'Work experience updated successfully!')
            return redirect('profile_1')
        else:
            messages.error(request, 'There were errors in the form. Please correct them.')
    else:
        form = WorkExperienceForm()

    return render(request, 'add_work_experience.html', {'form': form})

@login_required
def update_work_experience(request, pk):
    profile, created = Profile.objects.get_or_create(id=1)
    
    # Ensure the work_experience_instance is related to the profile
    work_experience_instance = profile.work_experiences.get(pk=pk)

    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, instance=work_experience_instance)
        if form.is_valid():
            form.save()
            return redirect('profile_1')
    else:
        form = WorkExperienceForm(instance=work_experience_instance)

    return render(request, 'update_work_experience.html', {'form': form})

@login_required
def add_education(request):
    profile, created = Profile.objects.get_or_create(id=1)

    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education_instance = form.save()
            profile.education.add(education_instance)
            return redirect('profile_1')
    else:
        form = EducationForm()

    return render(request, 'add_education.html', {'form': form})

@login_required
def update_education(request, pk):
    profile, created = Profile.objects.get_or_create(id=1)
    
    # Ensure the work_experience_instance is related to the profile
    education_instance = profile.education.get(pk=pk)

    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education_instance)
        if form.is_valid():
            form.save()
            return redirect('profile_1')
    else:
        form = EducationForm(instance=education_instance)

    return render(request, 'update_education.html', {'form': form})

@login_required
def add_skill(request):
    profile, created= Profile.objects.get_or_create(id=1)

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill_instance = form.save()
            profile.skills.add(skill_instance)
            return redirect('profile_1')
    else:
        form = SkillForm()
    return render(request, 'add_skill.html', {'form':form})

@login_required
def add_achievement(request):
    profile, create = Profile.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = AchievementForm(request.POST)
        if form.is_valid():
            achievement_instance = form.save()
            profile.achievements.add(achievement_instance)
            return redirect('profile_1')
    else:
        form = AchievementForm()
    return render(request, 'add_achievement.html', {'form':form})


@login_required
def add_project(request):
    profile, create = Profile.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project_instance = form.save()
            profile.project.add(project_instance)
            return redirect('profile_1')
        else:
            form.errors
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form':form})

@login_required       
def add_hobby(request):
    profile, created = Profile.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = HobbyForm(request.POST)
        if form.is_valid():
            hobby_instance = form.save()
            profile.hobby.add(hobby_instance)
            return redirect('profile_1')
    else:
        form = HobbyForm()
    return render(request, 'add_hobby.html', {'form': form} )

@method_decorator(login_required, name='dispatch')
class DeleteExperienceView(DeleteView):
    model = WorkExperience
    success_url = reverse_lazy('profile_1')
    template_name = 'delete_confirm.html'

@method_decorator(login_required, name='dispatch')
class DeleteEducationView(DeleteView):
    model = Education
    success_url = reverse_lazy('profile_1')
    template_name = 'delete_confirm.html'

@method_decorator(login_required, name='dispatch')
class DeleteProjectView(DeleteView):
    model = Project
    success_url = reverse_lazy('profile_1')
    template_name = 'delete_confirm.html'

@method_decorator(login_required, name='dispatch')
class DeleteSkillView(DeleteView):
    model = Skill
    success_url = reverse_lazy('profile_1')
    template_name = 'delete_confirm.html'

@method_decorator(login_required, name='dispatch')
class DeleteAchievementView(DeleteView):
    model = Achievement
    success_url = reverse_lazy('profile_1')
    template_name = 'delete_confirm.html'

@method_decorator(login_required, name='dispatch')
class DeleteHobbyView(DeleteView):
    model = Hobby
    success_url = reverse_lazy('profile_1')
    template_name = 'delete_confirm.html'



def login_with_otp(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        next_url = request.GET.get('next')
        print('Next =',next_url)
        if next_url:
            request.session['next_url'] = next_url 

        if user is not None:
            # Generate and send OTP
            otp = get_random_string(length=6, allowed_chars='1234567890')
            send_otp_to_email(user.email, otp)

            # Store OTP and its creation timestamp securely in the session

            request.session['otp'] = otp
            request.session['otp_timestamp'] = datetime.datetime.now().timestamp()
            request.session['user_email'] = user.email
            print(user.email)
            return render(request, 'verify_otp.html', {'username': username, 'email': user.email})


        else:
            # Handle incorrect credentials
            pass
        
    return render(request, 'login.html')

def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        user_email = request.session.get('user_email')
        otp_timestamp = request.session.get('otp_timestamp')

        if entered_otp == stored_otp:
            # Check if OTP is expired (current time - timestamp > 3 minutes)
            if datetime.datetime.now().timestamp() - otp_timestamp > 600:
                messages.error(request, 'OTP has expired. Please request a new one.')
            else:
                User = get_user_model()
                try:
                    user = User.objects.get(email=user_email)
                    login(request, user)
                    del request.session['otp']
                    del request.session['otp_timestamp']
                    del request.session['user_email']
                    next_url = request.session.get('next_url')
                    print(next_url)
                    if next_url:
                        del request.session['next_url']  # Remove 'next_url' from session
                        return redirect(next_url)
                    else:
                        return redirect('/') 
                except User.DoesNotExist:
                    messages.error(request, 'User with provided email not found')
        else:
            messages.error(request, 'Invalid OTP')

    return render(request, 'verify_otp.html')

def contact(request):
    if request.method == 'POST': 
        profile, created = Profile.objects.get_or_create(id=1)
        email = profile.email
        sender_email = request.POST['email']
        phone = request.POST['phone']
        message_content= request.POST['message']     
        subject = 'Inquiry'
        message = f' {message_content}. \n Reach me Here {phone}. \n My email is {sender_email}.'
        recipient_list = [email]
        send_mail(subject, message,'', recipient_list)
        return redirect('success')  

    return render(request, 'contact.html')


def send_otp_to_email(email, otp):
    # Customize this function to send the OTP to the user's email
    subject = 'Your OTP for Login'
    message = f'Your OTP is: {otp}'
    from_email = 'your@example.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

#error handlers
def custom_404_view(request, exception):
    return render(request, 'error_template/404.html', status=404)

def custom_500_view(request):
    return render(request, 'error_template/500.html', status=500)

def permission_denied_view(request, exception):
    return render(request, 'error/403.html', status=403)