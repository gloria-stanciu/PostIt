from django.contrib import admin
from .models import PostIt

# Register your models here.

class PostItAdmin(admin.ModelAdmin):
    list_display = ('title', 'noteText', 'completed', 'created')

admin.site.register(PostIt, PostItAdmin)
