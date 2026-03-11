from django import forms
from .models import Application
import os

class ApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.required_docs = kwargs.pop('required_docs', [])
        super().__init__(*args, **kwargs)
        # Dynamically add a FileField for each required document
        for doc in self.required_docs:
            field_name = f'doc_{doc.lower().replace(" ", "_")}'
            self.fields[field_name] = forms.FileField(label=f'Upload {doc}', required=True)

    def clean(self):
        cleaned_data = super().clean()
        # Ensure all required docs are uploaded
        for doc in self.required_docs:
            field_name = f'doc_{doc.lower().replace(" ", "_")}'
            if not self.files.get(field_name):
                self.add_error(field_name, f'{doc} is required.')
        return cleaned_data

    class Meta:
        model = Application
        fields = []  # We'll handle files manually
