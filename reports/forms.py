from django import forms
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ["title", "description", "issue_type", "location", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Issue title"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Describe the issue"}),
            "issue_type": forms.Select(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control", "placeholder": "Location"}),
        }
