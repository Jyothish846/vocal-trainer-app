from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    VOCAL_TYPE_CHOICES = [
        ('not_sure', 'Not Sure'),
        ('bass', 'Bass'),
        ('tenor', 'Tenor'),
        ('alto', 'Alto'),
        ('soprano', 'Soprano'),
    ]
    vocal_type=models.CharField(
            max_length=20,
            choices=VOCAL_TYPE_CHOICES,
            default='not_sure',
        )
    lowest_note = models.IntegerField(null=True, blank=True)
    highest_note = models.IntegerField(null=True, blank=True)