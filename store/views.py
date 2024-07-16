from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.views import generic
from .models import Project, Category, Service, About, CV, Messages
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class Home(generic.TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                
                'featured_categories': Category.objects.filter(featured=True),
                'featured_services': Service.objects.filter(featured=True),
                'featured_about': About.objects.filter(featured=True),
                'featured_cv': CV.objects.filter(featured=True),
                
            }
        )
        context['current_path'] = self.request.path
        return context


def download_cv(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    response = FileResponse(cv.file.open(), as_attachment=True)
    return response


class Project_details(generic.DetailView):
    model = Project
    template_name = 'project_details.html'
    slug_url_kwarg = 'slug'



class Contact(generic.FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')  # Redirect to the contact page after success
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_path'] = self.request.path
        
        return context
    

    def form_valid(self, form):
        
        form.save()
        
        messages.success(self.request, "Your message has been sent to the admin")
        return super().form_valid(form)
