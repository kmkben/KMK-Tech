from django.contrib import admin 
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms
from .models import Project, ProjectCategory

# Register your models here.


class ProjectAdminForm(forms.ModelForm):
    # description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Project
        fields = '__all__'


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "category", "created_at")

# admin.site.register(Project, ProjectAdmin)
# admin.site.register(ProjectCategory, ProjectCategoryAdmin)  