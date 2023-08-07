from django.contrib import admin
from .models import Todo

#class TodoAdmin(admin.ModelAdmin):
 #   list_display = ('title', 'description', 'completed','created_at','owner')

# Register your models here.

admin.register(Todo)