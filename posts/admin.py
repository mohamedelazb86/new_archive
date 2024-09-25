from django.contrib import admin

from .models import Post,Category,Review

class PostAdmin(admin.ModelAdmin):
    list_display=['user','title','draft']
    search_fields=['title','content']
    list_filter=['draft']

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Review)
