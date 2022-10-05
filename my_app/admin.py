from django.contrib import admin
from . import models

# Register your models here.

class adminCreatPostDisplay(admin.ModelAdmin):
    list_display = ['caption', 'owner', 'id']

admin.site.register(models.CreatePost, adminCreatPostDisplay)