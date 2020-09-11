from django.db import models

# Create your models here.

class PostIt(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    noteText = models.CharField(max_length=500, null=True, blank=True)
    completed = models.BooleanField(default=False, blank= False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s %s' % (self.title, self.noteText, self.completed, self.created)
