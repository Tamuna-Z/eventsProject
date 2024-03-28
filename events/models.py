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

class RSVP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
class Comments(models.Model):
    User= models.ForeignKey(User, on_delete=models.CASCADE)
    event= models.ForeignKey(Event, on_delete=models.CASCADE)
    body= models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:20]




