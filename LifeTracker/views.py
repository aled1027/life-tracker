from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from forms import MyRegistrationForm


def accounts_home(request):
	return render(request, "accounts_home.html", {})

def login(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

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
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("register_success"))
		else:
			return HttpResponseRedirect(reverse("register_error"))

	args = {}
	args.update(csrf(request))
	args['form'] = MyRegistrationForm()
	return render(request, 'register.html', args)

def register_success(request):
	return render(request, 'register_success.html', {})

def register_error(request):
	return render(request, 'register_error.html', {})
