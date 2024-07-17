from django.db import models
from tinymce.models import HTMLField  
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True, max_length=150)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title


class Project(models.Model):
    category = models.ForeignKey(Category, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(unique=True, max_length=150)
    image = models.ImageField(upload_to='project_images')
    featured = models.BooleanField(default=False)
    created_date = models.CharField(max_length=50)
    github = models.URLField(max_length=300, blank=True, null=True)
    live_link = models.URLField(max_length=300, blank=True, null=True)
    description = HTMLField()
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.title


class Service(models.Model):
    
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='service_images')
    description = models.TextField(max_length=100)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=100)
    description1 = models.TextField(max_length=500)
    description2 = models.TextField(max_length=500)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CV(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='resume')
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Messages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name


class BioData(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=350)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_image')
    email = models.EmailField()
    featured = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name