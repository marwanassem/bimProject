from django.shortcuts import render
from .forms import ProjectForm
from .models import Project
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'base.html')


def bim_cal(request):
    form = ProjectForm()
    total_percent = 0

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data['type']
            size = form.cleaned_data['project_size']
            document_work = form.cleaned_data['document_work']
            reduced_rework = form.cleaned_data['reduced_rework']
            fewer_claims = form.cleaned_data['fewer_claims']

            cost = form.cleaned_data['cost']
            duration = form.cleaned_data['duration']

            total_percent += Project.get_type_percent(Project, type)
            print(total_percent)

            total_percent += Project.get_size_percent(Project, size)
            print(Project.get_size_percent(Project, size))

            total_percent += Project.get_attributes_percent(Project, document_work)
            print(document_work)
            print(Project.get_attributes_percent(Project, document_work))

            total_percent += Project.get_attributes_percent(Project, reduced_rework)
            print(Project.get_attributes_percent(Project, reduced_rework))

            total_percent += Project.get_attributes_percent(Project, fewer_claims)
            print(Project.get_attributes_percent(Project, fewer_claims))
            total_percent = float(total_percent)

            print(total_percent)

            doc_work = total_percent * 60.4
            doc_work = "{:.2f}".format(doc_work)
            rework = total_percent * 35.4
            rework = "{:.2f}".format(rework)
            claims = total_percent * 16.11
            claims = "{:.2f}".format(claims)

            new_cost_percent = total_percent * 30.4
            new_duration_percent = total_percent * 21.1

            new_cost_percent = 1 - (new_cost_percent/100)
            new_duration_percent = 1 - (new_duration_percent/100)

            new_cost = float(cost) * new_cost_percent
            new_cost = round(new_cost)
            new_duration = float(duration) * new_duration_percent
            new_duration = round(new_duration)

            context = {
                'doc_work': doc_work,
                'rework': rework,
                'claims': claims,
                'original_cost': cost,
                'original_duration': duration,
                'new_cost': new_cost,
                'new_duration': new_duration,
            }

            return render(request, 'bimCalc/bim_output.html', context=context)

    form = ProjectForm()
    return render(request, 'bimCalc/bim.html', {'form': form})

