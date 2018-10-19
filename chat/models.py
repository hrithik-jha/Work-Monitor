from django.db import models

class Text(models.Model):
    text = models.CharField(max_length = 200)
    time = models.DateTimeField()

    def __unicode__(self):
        return self.name

    def meet_date_pretty(self):
        return self.meet_date.strftime('%b %e %Y')