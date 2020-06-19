from django.db import models
from django.contrib.auth import get_user_model

class Lecture(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='presenterx/images/', blank=True)
    url = models.URLField(max_length=150, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
            return self.title + ' by ' + str(self.user)
