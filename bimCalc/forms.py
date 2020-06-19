from django import forms
from bimCalc.models import Project


class ProjectForm(forms.ModelForm):
    type = forms.ChoiceField(choices=Project.types, label='Type of Project')
    project_size = forms.ChoiceField(choices=Project.size, label='Size of Project')
    cost = forms.CharField(max_length=10, label='Cost of Project in LE')
    duration = forms.CharField(max_length=1000, label='Duration in days')
    document_work = forms.ChoiceField(choices=Project.choices, label='Reduced Document Work')
    reduced_rework = forms.ChoiceField(choices=Project.choices, label='Reduced Rework')
    fewer_claims = forms.ChoiceField(choices=Project.choices, label='Fewer Claims - Litigation')

    class Meta:
        model = Project
        exclude = ['COST_PERCENT', 'DURATION_PERCENT', ]