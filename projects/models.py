from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

""" Projects application model definitions.

This module defines the models employed by the projects application. The 
application consists of 3 core models. Project, milestone and task. Projects
consist of milestones consist of tasks. 

This module employs abstract classes to allow for future modification to common
elements. Trackable, Completable, Commentable and Impactful are 4 interfaces
or mixins defined in this module. These mixins employ generic relations to
allow the 3 core models to all benefit from their functionality without tying
them to the related models. For example, any future changes to the Completion
model will propogate through the inheritance tree to all Completable models. 
This ensures that the project model will never have to be concerned with the
way completions are implemented. Concurrently, the database is completely 
decoupled from the implementation of these mixins thanks to the use of 
generics.  

"""

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

class Trackable(models.Model):

    """ Logging mixin.
   
    Factors out 2 common fields that are used in logging. Any future logging 
    requirements can be worked out here and will propogate through the 
    inheritance tree. 

    """

    user = models.ForeignKey(User)
    stamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

class FeedEntry(Trackable):

    """ News feed type model used to track user behaviors.

    Feed entries are created on various triggers including add, update and 
    delete. These feed entries can then be queried to log the behaviors of 
    users. 

    """

    action = models.SlugField()
    instance = models.SlugField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()

class Completion(Trackable):

    """ Represents completion of a unit of work.
    
    Completable models can be signified as complete by adding a reference to 
    this model. For example, a project is said to be complete when it has at 
    least one reference to a completion.  

    """
    comment = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()

    def __unicode__(self):
        return "%s" % (
            self.content_type.get_object_for_this_type(pk=self.object_id)
        )

class Comment(Trackable):
 
    """ Allows for commentary on any commentable model.

    Commentable models can add as many comments as necessary.  

    """

    comment = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()

    def __unicode__(self):
        return "%s" % (
            self.content_type.get_object_for_this_type(pk=self.object_id)
        )

class ImpactStatement(Trackable):

    """ Impact that any unit of work will have on a department. 

    Stores information about the impact that a given unit of work will have on
    a given department. Projects, milestones and tasks without any impact 
    statements probably need more research. 

    """
 
    department = models.ForeignKey(Department)
    statement = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
 
    def __unicode__(self):
        return "%s" % (self.department)

class Completable(models.Model):

    """ Completion mixin.

    The inheriting class will gain a generic relation to the Completion model
    and access to methods that provide data about the inheriting class 
    instance's completions. 

    """

    completions = generic.GenericRelation(Completion)

    class Meta:
        abstract = True

    def is_complete(self):
        return True if self.completions.all() else False 


class Impactful(models.Model):

    """ Impact statement mixin.
   
    The inheriting class will gain a generic relation to the impact
    statement model and access to methods that provide data about 
    the inheriting class instance's impact statements. 

    """

    impact_statements = generic.GenericRelation(ImpactStatement)

    class Meta:
        abstract = True

    def is_impactful(self): 
        return True if self.impact_statements.all() else False 

class Commentable(models.Model):

    """ Comment mixin.
    
    The inheriting class will gain a generic relation to the comment model and
    and access to methods that provide data about the inheriting class 
    instance's comments.

    """

    comments = generic.GenericRelation(Comment)

    class Meta:
        abstract = True

    def is_commented(self):
        return True if self.comments.all() else False

class Project(Completable, Commentable, Impactful, Trackable):
    department = models.ForeignKey(Department)
    name = models.CharField(max_length=32)
    description = models.TextField()
    planned_completion_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return "%s" % (self.name)

class Milestone(Completable, Commentable, Impactful, Trackable):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=32)
    description = models.TextField()
    planned_completion_date = models.DateField()

    def __unicode__(self):
        return "%s" % (self.name)
 
    class meta:
        ordering = "project"

class Task(Completable, Commentable, Impactful, Trackable):
    milestone = models.ForeignKey(Milestone)
    name = models.CharField(max_length=32)
    description = models.TextField()
    responsible = models.ForeignKey(User, related_name="responsible_user") 
    planned_completion_date = models.DateField()
    
    def __unicode__(self):
        return "%s" % (self.name)
   
@receiver(post_save)
def feed_activity_handler(sender, instance, created, **kwargs):
    if sender in (
        Project, Milestone, Task, Comment, Completion, ImpactStatement
    ):
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
    if sender in (
        Project, Milestone, Task, Comment, Completion, ImpactStatement
    ):
        FeedEntry(
            stamp=instance.stamp, user=instance.user, action="removed", 
            content_type=ContentType.objects.get(
                model=sender.__name__.lower()
            ), instance=instance.__unicode__(), object_id=instance.id
        ).save()
