from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class About2PageView(TemplateView):
    template_name = 'about2.html'

class DonPageView(TemplateView):
    template_name = 'Don.html'