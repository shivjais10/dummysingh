from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from accounts.forms import (
    RegistrationForm,
    EditProfileForm
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
'''
def home(request):
    #return HttpResponse('Home page')
    return render(request,'accounts/login.html')
'''

def home(request):

    return render(request,'accounts/home.html')
def logout(request):
    #return HttpResponse('Home page')
    return render(request,'accounts/logout.html')

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

def profile(request):

    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()

            # ''' update_session_auth_hash is use to
            # update the session with the new password hash so that a
            # user changing their own password wont log themselves out.
            # '''
            update_session_auth_hash(request, form.user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/accounts/profile')
            #return HttpResponseRedirect(reverse('profile'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
