from django.contrib import admin

# Register your models here.
from django.contrib import admin
from blog.models import Tag, Post
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)