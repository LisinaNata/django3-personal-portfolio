from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=100)
    discriptions=models.CharField(max_length=250)
    image=models.ImageField(upload_to='portfolio/images/')
    url=models.URLField(blank=True)

# Create your models here.
def __str__(self):
    return self.title
