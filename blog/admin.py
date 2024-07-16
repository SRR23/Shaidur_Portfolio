from django.contrib import admin
from .models import Category, Tag, Blog
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)
