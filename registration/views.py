from django.contrib.auth.models import User
from django.shortcuts import render
from registration.forms import UserForm,UserProfileInfoForm
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from . import models
from django.core.mail import send_mail
from django.conf import settings



from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def about(request):
    return render(request,'registration/about.html')

def eshop(request):
    return render(request,'registration/eshop.html')

"""class eshopView(TemplateView):
    template_name = 'eshop.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        return context

"""
def register(request):

    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            name=user_form.cleaned_data['firstname']
            subject='message from eshop'
            comment ='Hi! I am a new user'
            message='%s %s' %(comment,name)
            emailFrom = user_form.cleaned_data['email']
            emailTo = [settings.EMAIL_HOST_USER]
            send_mail(
                subject,
                message,
                emailFrom,
                emailTo,
                fail_silently=True,
                )

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit = False)
            profile.user = user
             
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered= True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'registration/register.html',
                                                        {'user_form': user_form,
                                                        'profile_form':profile_form,
                                                       'registered': registered})
def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('eshop'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('Someone tried to login and failed!')
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'registration/login.html',{})

@login_required
def special(request):
    return HttpResponse("You are logged in!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('eshop'))






"""
    form =forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Success")
            print("Name*" + form.cleaned_data['name'])
            print("Username*" + form.cleaned_data['username'])
            print("Email*" + form.cleaned_data['email'])
            print("Phone Number*" + form.cleaned_data['phone_number'])
        form.save()
"""

