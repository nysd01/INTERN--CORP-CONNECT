from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, CompanyProfileForm, InternProfileForm
from .models import User, CompanyProfile, InternProfile
from django import forms
@login_required
def profile_page(request):
	user = request.user
	if user.is_company:
		profile = CompanyProfile.objects.get(user=user)
		ProfileForm = CompanyProfileForm
		profile_type = 'company'
	else:
		profile = InternProfile.objects.get(user=user)
		ProfileForm = InternProfileForm
		profile_type = 'intern'
	class UserForm(forms.ModelForm):
		class Meta:
			model = User
			fields = ['username', 'email']
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Profile updated successfully!')
			return redirect('profile_page')
	else:
		user_form = UserForm(instance=user)
		profile_form = ProfileForm(instance=profile)
	return render(request, 'profile_page.html', {
		'user_form': user_form,
		'profile_form': profile_form,
		'profile': profile,
		'profile_type': profile_type,
		'user': user,
	})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .models import User, CompanyProfile, InternProfile

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user_type = form.cleaned_data['user_type']
			if user_type == 'company':
				user.is_company = True
			else:
				user.is_intern = True
			user.save()
			if user.is_company:
				CompanyProfile.objects.create(user=user, name=user.username)
			else:
				InternProfile.objects.create(user=user)
			login(request, user)
			return redirect('company_dashboard' if user.is_company else 'intern_dashboard')
	else:
		form = RegisterForm()
	return render(request, 'register.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('company_dashboard' if user.is_company else 'intern_dashboard')
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form': form})

def logout_view(request):
	logout(request)
	return redirect('login')
