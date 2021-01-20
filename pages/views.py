from django.shortcuts import render
from django.http import HttpResponse        # from the django.http module import the HttpResponse class
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"
    

class AboutView(TemplateView):
    template_name = "about.html"
   

# Create your views here.
# def view_function(request):
#     html = "<h1>Hello, World!</h1>"
#     return HttpResponse(html)
