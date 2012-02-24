from django.forms import ModelForm
from projects.models import *

class ProjectCreateForm(ModelForm):
    class Meta:
        model = Project
    
