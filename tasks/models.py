from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(null=True)
    date_posted = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


