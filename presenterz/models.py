from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.utils import timezone
from django.shortcuts import reverse

class Lecture(models.Model):
    title = models.CharField(max_length=250)
    description = HTMLField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='presenterx/images/', blank=True)
    url = models.URLField(max_length=150, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
            return self.title + ' by ' + str(self.user)


class Session(models.Model):
    lecture = models.ForeignKey(Lecture, related_name='sessions', on_delete=models.CASCADE)
    location = models.CharField(max_length = 30, default='Not specified')
    time = models.DateTimeField(default=timezone.now)
    length = models.IntegerField(default=60)
    link = models.URLField(max_length=200, blank=True)
    participants = models.ManyToManyField(get_user_model(), through='Participation')

    def __str__(self):
        return str(self.lecture) + ' - ' + self.location + ' - ' + str(self.time)

    def get_absolute_url(self):
        return reverse('presenterz:session_details', kwargs={'pk': self.pk})


class Participation(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)#(default=timezone.now)

    def __str__(self):
        return str(self.user) + ' --> ' + str(self.session)

    class Meta:
        unique_together = [['user', 'session']]
