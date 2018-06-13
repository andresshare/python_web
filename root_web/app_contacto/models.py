from django.db import models

# Create your models here.

class Topic(models.Moldel):
    top_name = models.CharField(max_length=264, Unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    Topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264, Unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
