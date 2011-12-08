from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from projects.models import *

class MilestoneInline(admin.StackedInline):
    model = Milestone
    extra = 1

class TaskInline(admin.StackedInline):
    model = Task
    extra = 1

class CompletionInline(generic.GenericStackedInline):
    model = Completion
    extra = 1

class CommentInline(generic.GenericStackedInline):
    model = Comment
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'department', 'planned_completion_date', 'is_complete',
    )
    inlines = [MilestoneInline, CommentInline, CompletionInline,]

class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('project', 'name', 'stamp', 'planned_completion_date',)
    inlines = [TaskInline, CommentInline, CompletionInline,]

class TaskAdmin(admin.ModelAdmin):
    list_display = ('milestone', 'name', 'stamp', 'planned_completion_date', 'is_complete')
    inlines = [CommentInline, CompletionInline,]
 
admin.site.register(Area)
admin.site.register(Department)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Milestone, MilestoneAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Completion)
admin.site.register(Comment)
admin.site.register(FeedEntry)
