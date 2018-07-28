import re

from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info
        path = request.path_info.lstrip('/')
        print "THIS"
        print path
        global url_is_exempt
        url_is_exempt=[]
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

#        if path == 'accounts/logout/':
 #          logout(request)
        #strip as django inbuilt middle wear add one /
        #if path == reverse('logout').lstrip('/'):
         #  logout(request)
          # print "LOGOOUT"
        print "THIS IS PATH ",path
        #if path == reverse('accounts : logout').lstrip('/'):
         #   logout(request)
          #  print "LOGOOUT"

        #if not request.user.is_authenticated():
         #   if not any(url.match(path) for url in EXEMPT_URLS):
        #        return redirect(settings.LOGIN_URL)
        print url_is_exempt
        print "AUTHI", request.user.is_authenticated()
        if request.user.is_authenticated() and url_is_exempt:
            print "A"
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated() or url_is_exempt:
            print "B"
            return None
        else:
            print "C"
            return redirect(settings.LOGIN_URL)