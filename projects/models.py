from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

# Create your models here.


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, blank=True)
    
    summary = models.TextField()
    objective = models.TextField(blank=True)
    context = models.TextField(blank=True)
    description = models.TextField(blank=True)
    tasks = models.TextField(blank=True) 
    
    technologies = TaggableManager(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title