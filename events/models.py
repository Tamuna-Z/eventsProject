from datetime import timezone

from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_time = models.DateTimeField()

    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name




class Attendee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    events_attending = models.ManyToManyField('Event', related_name='attendees', blank=True)

    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.body[0:20]
