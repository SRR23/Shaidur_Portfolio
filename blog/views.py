from django.shortcuts import render, redirect
from django.views import generic
from .models import Category, Tag, Blog
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator, InvalidPage

# Create your views here.


class Custom_Paginator:
    def __init__(self, request, queryset, paginated_by):
        self.paginator = Paginator(queryset, paginated_by)
        self.paginated_by = paginated_by
        self.queryset = queryset
        self.page = request.GET.get('page', 1)
        
    def get_queryset(self):
        try:
            queryset = self.paginator.page(self.page)
        except PageNotAnInteger:
            queryset = self.paginator.page(1)
        except EmptyPage:
            queryset = self.paginator.page(1)
        except InvalidPage:
            queryset = self.paginator.page(1)
        
        return queryset
    
    
    
class Blogs(generic.ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'
    
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        page_obj = Custom_Paginator(self.request, self.get_queryset(), self.paginate_by)
        queryset = page_obj.get_queryset()
        paginator = page_obj.paginator
        context['blog'] = queryset
        context['paginator'] = paginator
        context['current_path'] = self.request.path
        
        
        return context


class Blog_details(generic.DetailView):
    model = Blog
    template_name = 'blog_details.html'
    context_object_name = 'B'
    slug_url_kwarg = 'slug'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_blogs'] = self.get_object().related
        
        return context
    

class Category_details(generic.DetailView):
    model = Category
    template_name = 'category_details.html'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['category_blogs'] = self.get_object().category_blogs.all()
        
        return context



