from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(max_length=150, blank=True)

    def __str__(self):
        return self.title
