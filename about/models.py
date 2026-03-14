from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField()
    # description = RichTextField()
    start_date = models.CharField(max_length=20)  # e.g. "2018"
    end_date = models.CharField(max_length=20, blank=True, default="Present")
    website = models.URLField(blank=True)
    order_number = models.IntegerField()
    

    class Meta:
        ordering = ['-order_number']

    def __str__(self):
        return f"{self.company} ({self.start_date} - {self.end_date})"


class Education(models.Model):
    school = models.CharField(max_length=150)
    degree = models.CharField(max_length=150)
    description = models.TextField()
    # description = RichTextField()
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20, blank=True, default="Present")
    website = models.URLField(blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.school} ({self.start_date} - {self.end_date})"
