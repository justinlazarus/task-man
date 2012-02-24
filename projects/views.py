from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from projects.models import *
from django.views.generic import CreateView
from projects.forms import *

@login_required
def index(request):
    return render(request, 'projects/index.html')

@login_required
def complete(request):
    if request.method == 'POST':
        POST = request.POST
        if (POST.get('comment') and POST.get('model_name') and 
            POST.get('object_id')
        ):
            completion = Completion(
                comment = POST.get('comment'), 
                content_type = ContentType.objects.get(
                    app_label="projects", model = POST.get('model_name')
                ), 
                object_id = POST.get('object_id'), user_id = request.user.id 
            )
            completion.save()

    return HttpResponse()

@login_required
def delete_project(request):
    if request.method == 'POST':
        POST = request.POST
        if POST.get('project_id'):
            project = Project.objects.get(pk=POST.get('project_id'))
            project.delete()

    return HttpResponse()

class CreateProject(CreateView):
    template_name = "projects/create_project.html"
    form_class = ProjectCreateForm
