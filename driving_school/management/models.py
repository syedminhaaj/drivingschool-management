from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.hours * self.instructor.hourly_rate
        super().save(*args, **kwargs)
