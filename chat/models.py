from django.db import models
from django.contrib.auth.models import User

class Text(models.Model):
    text = models.CharField(max_length = 200, null = True, default = '')
    time = models.DateTimeField()
    member = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)

    #def unicode(self):
    #    return self.text

    def meet_date_pretty(self):
        return self.time.strftime('%b %e %Y')