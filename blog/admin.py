from django.contrib import admin
from blog.models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'body', 'publish', 'created','updated','status',)
admin.site.register(Post,PostAdmin)







