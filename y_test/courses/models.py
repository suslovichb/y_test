from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    lectures_number = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["start_date"]
