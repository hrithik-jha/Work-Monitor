from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name