from django.db import models
from django.contrib.auth.models import User

class Meeting(models.Model):
    title = models.CharField(max_length = 100)
    meet_date = models.DateTimeField()
    agenda = models.TextField()
    url = models.TextField()
    venue = models.TextField()
    attendance = models.IntegerField()
    member = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)

    def __str__(self):
        return self.title

    def summary(self):
        return self.agenda[:100]

    def meet_date_pretty(self):
        return self.meet_date.strftime('%b %e %Y')

'''
class Work(models.Model):
    task = models.CharField(max_length = 100)
    deadline = models.DateTimeField()
    objtvs = models.TextField()
    url = models.TextField()
    completion = models.IntegerField()
    member = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def deadline(self):
        return self.deadline.strftime('%b %e %Y')

    def summary(self):
        return self.objtvs[:100]    
'''