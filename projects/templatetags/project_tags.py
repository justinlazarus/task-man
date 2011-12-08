from django import template
from projects.models import User

register = template.Library()

@register.filter
def get_task_count(user):
    return user.task_set.filter(reponsibles=user).count()
