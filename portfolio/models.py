from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    rep_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='portfolio/images')

    def __str__(self):
        return self.title
