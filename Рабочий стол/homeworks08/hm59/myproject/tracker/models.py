from django.db import models

class Project(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Task(models.Model):
    ...
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    ...

