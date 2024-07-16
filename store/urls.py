from django.urls import path
from .views import Home, download_cv, Project_details, Contact
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('download-resume/<int:pk>/', download_cv, name='download_resume'),
    path('project-details/<str:slug>/', Project_details.as_view(), name="project_details"),
    path('contact/', Contact.as_view(), name='contact'),
]