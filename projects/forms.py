from django.forms import ModelForm
from django import forms

from projects.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'demo_link', 'featured_image', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }

    # Adds a class name based on the input type
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
