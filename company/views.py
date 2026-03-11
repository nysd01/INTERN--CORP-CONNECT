from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from internships.forms import InternshipForm

@login_required
def dashboard(request):
	return render(request, 'company_dashboard.html', {'user': request.user})

@login_required
def post_internship(request):
	if request.method == 'POST':
		form = InternshipForm(request.POST, request.FILES)
		if form.is_valid():
			internship = form.save(commit=False)
			internship.company = request.user
			internship.save()
			return redirect('company_dashboard')
	else:
		form = InternshipForm()
	return render(request, 'post_internship.html', {'form': form, 'user': request.user})
