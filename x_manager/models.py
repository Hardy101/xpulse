from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class ScheduledTweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tweet_text = models.CharField(max_length=280)
    schedule_time = models.DateTimeField()
    is_posted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tweet_text} - {self.user.username}"
