from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Area(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return "%s" % (self.name)

class Department(models.Model):
    area = models.ForeignKey(Area)
    number = models.SmallIntegerField()
    name = models.CharField(max_length=32)
    
    def __unicode__(self):
        return "%s" % (self.name)

class completable():
    def is_complete(self):
        return True if self.completions.all() else False 

class FeedEntry(models.Model):
    stamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    action = models.SlugField()
    instance = models.SlugField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User)
    stamp = models.DateTimeField(auto_now_add=True) 
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()

    def __unicode__(self):
        return "%s (%s)" % (
            self.content_type.get_object_for_this_type(pk=self.object_id),
            self.content_type
        )

class Completion(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User)
    stamp = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()

    def __unicode__(self):
        return "%s %s" % (
            self.content_type,
            self.content_type.get_object_for_this_type(pk=self.object_id)
        )

class Project(models.Model, completable):
    department = models.ForeignKey(Department)
    name = models.CharField(max_length=32)
    description = models.TextField()
    stamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    planned_completion_date = models.DateField(null=True, blank=True)
    completions = generic.GenericRelation(Completion)
    comments = generic.GenericRelation(Comment)

    def __unicode__(self):
        return "%s" % (self.name)

class Milestone(models.Model, completable):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=32)
    description = models.TextField()
    stamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    planned_completion_date = models.DateField()
    completions = generic.GenericRelation(Completion)
    comments = generic.GenericRelation(Comment)

    def __unicode__(self):
        return "%s" % (self.name)
 
class Task(models.Model, completable):
    milestone = models.ForeignKey(Milestone)
    name = models.CharField(max_length=32)
    description = models.TextField()
    reponsibles = models.ManyToManyField(
        User, related_name="responsible_users" 
    )
    user = models.ForeignKey(User)
    stamp = models.DateTimeField(auto_now_add=True)
    planned_completion_date = models.DateField()
    completions = generic.GenericRelation(Completion)
    comments = generic.GenericRelation(Comment)
    
    def __unicode__(self):
        return "%s" % (self.name)
   
@receiver(post_save)
def feed_activity_handler(sender, instance, created, **kwargs):
    if sender in (Project, Milestone, Task, Comment, Completion):
        if created:
            action="added"
        else:
            action="modified"
        
        FeedEntry(
            stamp=instance.stamp, user=instance.user, action=action, 
            content_type=ContentType.objects.get(
                model=sender.__name__.lower()
            ), instance=instance.__unicode__(), object_id=instance.id
        ).save()

@receiver(pre_delete)
def feed_activity_handler_delete(sender, instance, **kwargs):
    if sender in (Project, Milestone, Task, Comment, Completion):
        FeedEntry(
            stamp=instance.stamp, user=instance.user, action="removed", 
            content_type=ContentType.objects.get(
                model=sender.__name__.lower()
            ), instance=instance.__unicode__(), object_id=instance.id
        ).save()
