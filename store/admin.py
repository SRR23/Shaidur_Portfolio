from django.contrib import admin
from .models import Category, Project, Service, About, CV, Messages, BioData
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service)
admin.site.register(About)
admin.site.register(CV)
admin.site.register(Messages)
admin.site.register(BioData)