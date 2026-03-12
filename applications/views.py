from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
@login_required
@csrf_exempt
def resubmit_documents(request, application_id):
    application = get_object_or_404(Application, id=application_id, applicant=request.user)
    if application.status != 'resubmission':
        return redirect('application_status')
    if request.method == 'POST' and request.FILES.get('resubmitted_document'):
        f = request.FILES['resubmitted_document']
        filename = default_storage.save(os.path.join('application_docs', f.name), f)
        application.uploaded_document = filename
        application.status = 'pending'
        application.save()
        # Notify company
        Notification.objects.create(
            user=application.internship.company,
            message=f"{request.user.username} has resubmitted documents for {application.internship.title}.",
            link=f"/applications/status/"
        )
        Notification.objects.create(
            user=request.user,
            message=f"Your resubmitted documents for {application.internship.title} have been sent.",
            link=f"/applications/status/"
        )
        return redirect('application_status')
    return redirect('application_status')
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from .models import Application
from internships.models import Internship
from messaging.models import Message, Notification
from django.core.files.storage import default_storage
from django.conf import settings
import os

@login_required
def apply(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)
    required_docs = [doc.strip() for doc in internship.required_documents.split(',') if doc.strip()]
    # Prevent duplicate application
    existing_application = Application.objects.filter(internship=internship, applicant=request.user).first()
    if existing_application:
        return render(request, 'apply.html', {
            'form': None,
            'internship': internship,
            'required_docs': required_docs,
            'error': 'You have already applied for this internship.'
        })
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES, required_docs=required_docs)
        if form.is_valid():
            application = Application(
                internship=internship,
                applicant=request.user,
                status='pending',
            )
            application.save()
            # Save each uploaded file (last one is stored in model for now)
            from .models import ApplicationDocument
            for doc in required_docs:
                field_name = f'doc_{doc.lower().replace(" ", "_")}'
                f = request.FILES.get(field_name)
                if f:
                    app_doc = ApplicationDocument.objects.create(
                        application=application,
                        file=f,
                        doc_type=doc
                    )
            Message.objects.create(
                sender=request.user,
                recipient=internship.company,
                content=f"I have applied for {internship.title}. Please find my documents attached."
            )
            Notification.objects.create(
                user=internship.company,
                message=f"New application received for {internship.title} from {request.user.username}",
                link=f"/company/applications/?app_id={application.id}"
            )
            Notification.objects.create(
                user=request.user,
                message=f"Application for {internship.title} submitted successfully!",
                link=f"/applications/status/?app_id={application.id}"
            )
            return redirect('application_status')
    else:
        form = ApplicationForm(required_docs=required_docs)
    return render(request, 'apply.html', {'form': form, 'internship': internship, 'required_docs': required_docs})

@login_required
def application_status(request):
    if hasattr(request.user, 'is_company') and request.user.is_company:
        # Company: show all applications to their internships
        applications = Application.objects.filter(internship__company=request.user).select_related('internship', 'applicant')
    else:
        # Intern: show their own applications
        applications = Application.objects.filter(applicant=request.user).select_related('internship')
    return render(request, 'application_status.html', {'applications': applications})


# New view: update application status
from django.views.decorators.http import require_POST
@login_required
@require_POST
def update_application_status(request, application_id):
    if not hasattr(request.user, 'is_company') or not request.user.is_company:
        return redirect('application_status')
    application = get_object_or_404(Application, id=application_id, internship__company=request.user)
    new_status = request.POST.get('status')
    missing_docs = request.POST.get('missing_docs', '').strip()
    valid_statuses = ['accepted', 'rejected', 'pending', 'resubmission']
    if new_status in valid_statuses and new_status != application.status:
        application.status = new_status
        application.save()
        # Send notification to intern
        if new_status == 'resubmission':
            msg = f"Your application for {application.internship.title} requires resubmission. Please upload the following missing documents: {missing_docs if missing_docs else 'See details.'}"
        else:
            msg = f"Your application for {application.internship.title} was updated to '{new_status.title()}'."
        Notification.objects.create(
            user=application.applicant,
            message=msg,
            link=f"/applications/status/"
        )
    return redirect('application_status')
