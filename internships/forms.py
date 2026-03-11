from django import forms
from .models import Internship

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = ['title', 'description', 'location', 'required_documents', 'document']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'required_documents': forms.TextInput(attrs={'placeholder': 'e.g. CV, Cover Letter'})
        }
