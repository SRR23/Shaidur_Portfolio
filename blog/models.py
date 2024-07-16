from django.db import models
from django.utils.text import slugify
from .slug import generate_unique_slug
from tinymce.models import HTMLField  
# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=150, unique=True)
    slug=models.SlugField(null=True, blank=True)
    created_date=models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)
        

class Tag(models.Model):
    title=models.CharField(max_length=150)
    slug=models.SlugField(null=True,blank=True)
    created_date=models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)


class Blog(models.Model):
    category=models.ForeignKey(Category,related_name='category_blogs',on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag,related_name='tag_blogs',blank=True)
    title=models.CharField(max_length=250)
    slug=models.SlugField(null=True, blank=True)
    banner=models.ImageField(upload_to='blog_banners')
    description=HTMLField()
    created_date=models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-id']
        
        
    def __str__(self) -> str:
        return self.title
    
    
    @property
    def related(self):
        return self.category.category_blogs.all().exclude(pk=self.pk)
    
    
    def save(self,*args,**kwargs):
        updating = self.pk is not None
        
        if updating:
            self.slug = generate_unique_slug(self, self.title, update=True)
            super().save(*args, **kwargs)
        else:
            self.slug=generate_unique_slug(self,self.title)
            super().save(*args,**kwargs)




