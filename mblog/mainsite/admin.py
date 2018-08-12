from django.contrib import admin

# Register your models here.

from .models import Post

class PistAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Post,PistAdmin)
