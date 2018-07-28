"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)
app_name = 'accounts'
from django.contrib.auth.views import login ,logout
urlpatterns = [

    url(r'^$', views.home),
#    url(r'^/login', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/', logout, {'template_name': 'accounts/logout.html'},name='logout'),

    url(r'^login',login, {'template_name': 'accounts/login.html'},name='login'),
     url(r'^register/', views.register,name='register'),
    url(r'^profile/$', views.profile, name='view_profile'),
url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),

#    url(r'^reset-password/$', password_reset, name='reset_password'),
    #using our reset page view is password_rest by default just our form
    #url(r'^reset-password-mypage/', password_reset, {'template_name': 'accounts/password_reset.html'},name='reset_password1'),
    url(r'^reset-password/$', password_reset, {'template_name': 'accounts/reset_password.html'},name='reset_password'),

    url(r'^reset-password/done/$', password_reset_done,name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),

    url(r'^reset-password/complete/$', password_reset_complete,{'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete')

]