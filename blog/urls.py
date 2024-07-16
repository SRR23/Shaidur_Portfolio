from django.urls import path
from .views import Blogs, Blog_details, Category_details
urlpatterns = [
    path('blog/', Blogs.as_view(), name='blog'),
    path('blog-details/<str:slug>/', Blog_details.as_view(), name="blog_details"),
    path('category-details/<str:slug>/', Category_details.as_view(), name="category_details"),
]