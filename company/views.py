
# View to show all documents for a specific application
from django.shortcuts import get_object_or_404
from applications.models import Application, ApplicationDocument
from django.contrib.auth.decorators import login_required

@login_required
def application_documents(request, application_id):
	application = get_object_or_404(Application, id=application_id, internship__company=request.user)
	documents = application.documents.all().order_by('uploaded_at')
	return render(request, 'application_documents.html', {
		'application': application,
		'documents': documents,
	})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from internships.forms import InternshipForm
from applications.models import Application
from internships.models import Internship
from django.contrib.auth import get_user_model

@login_required
def dashboard(request):
	from applications.models import Application, ApplicationDocument
	from internships.models import Internship
	internships = Internship.objects.filter(company=request.user)
	recent_applications = (
		Application.objects.filter(internship__in=internships)
		.select_related('internship', 'applicant')
		.prefetch_related('documents')
		.order_by('-date_applied')[:10]
	)
	return render(request, 'company_dashboard.html', {
		'user': request.user,
		'recent_applications': recent_applications,
	})

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

@login_required
def applications_view(request):
	# Get all internships posted by this company
	internships = Internship.objects.filter(company=request.user)
	applications = Application.objects.filter(internship__in=internships).select_related('internship', 'applicant').prefetch_related('documents')
	applicant_id = request.GET.get('applicant')
	if applicant_id:
		applications = applications.filter(applicant__id=applicant_id)
	return render(request, 'company_applications.html', {
		'applications': applications,
		'user': request.user,
	})
