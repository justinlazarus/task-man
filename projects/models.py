from django.db import models
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

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User)
    create_stamp = models.DateTimeField(auto_now_add=True) 
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()

    def __unicode__(self):
        return "%s" % (self.create_stamp)

class Completion(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User)
    complete_stamp = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()

    def __unicode__(self):
        return "%s" % (self.complete_stamp)

class Project(models.Model):
    department = models.ForeignKey(Department)
    name = models.CharField(max_length=32)
    description = models.TextField()
    create_stamp = models.DateTimeField(auto_now_add=True)
    planned_completion_date = models.DateField(null=True, blank=True)
    completions = generic.GenericRelation(Completion)
    comments = generic.GenericRelation(Comment)

    def __unicode__(self):
        return "%s" % (self.name)

    def is_complete(self):
        completions = self.completions.all()
        if completions:
            return True
        return False


class Milestone(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=32)
    description = models.TextField()
    create_stamp = models.DateTimeField(auto_now_add=True)
    planned_completion_date = models.DateField()
    completions = generic.GenericRelation(Completion)
    comments = generic.GenericRelation(Comment)

    def __unicode__(self):
        return "%s" % (self.name)
 
    def is_complete(self):
        completions = self.completions.all()
        if completions:
            return True
        return False

class Task(models.Model):
    milestone = models.ForeignKey(Milestone)
    name = models.CharField(max_length=32)
    description = models.TextField()
    users = models.ManyToManyField(User)
    create_stamp = models.DateTimeField(auto_now_add=True)
    planned_completion_date = models.DateField()
    completions = generic.GenericRelation(Completion)
    comments = generic.GenericRelation(Comment)
    
    def __unicode__(self):
        return "%s" % (self.name)

    def is_complete(self):
        completions = self.completions.all()
        if completions:
            return True
        return False
