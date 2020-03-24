from django.contrib import admin
from .models import LabPost, FilePost

# Register your models here.
admin.site.register(LabPost)
admin.site.register(FilePost)