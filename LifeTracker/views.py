from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from forms import MyRegistrationForm



def accounts_home(request):
	return render(request, "accounts_home.html", {})

def login(request):
	c = {}
	return render(request, 'login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render(request, 'loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
	return render(request, 'invalid_login.html')

def logout(request):
	auth.logout(request)
	return render(request, 'logout.html')

def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			auth.logout(request)
			authenticate(username=user.username, password=user.password)
			return HttpResponseRedirect(reverse("register_success"))
		else:
			return HttpResponseRedirect(reverse("register_error"))
	args = {}
	args['form'] = MyRegistrationForm()
	return render(request, 'register.html', args)

def register_success(request):
	return render(request, 'register_success.html', {})

def register_error(request):
	return render(request, 'register_error.html', {})

def profile_view(request, username):
	u = get_object_or_404(User, username=username)
	return render(request, 'profile.html', {'user': u})
