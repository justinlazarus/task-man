from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from projects.models import *

@login_required
def index(request):
    return render(request, 'projects/index.html')

@login_required
def complete(request):
    if request.method == 'POST':
        POST = request.POST
        if POST.get('comment') and POST.get('model_name') and POST.get('object_id'):
            completion = Completion(
                comment = POST.get('comment'), content_type = ContentType.objects.get(
                    app_label="projects", model = POST.get('model_name')
                ), object_id = POST.get('object_id'), user_id = request.user.id 
            )
            completion.save()
            message = "it worked!"
        else:
            message = "parameter issue"
    else:
        message = "didn't get into the post"

    return HttpResponse(message)
