
# Create your views here.
from django.shortcuts import render # here by default
from django.views.generic import TemplateView

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Maria Alejandra Ocampo",
        })
        return context

class ContactPageView(TemplateView):
    template_name = "pages/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact",
            "subtitle": "Contact Us",
            "email": "marialeja@example.com",
            "address": "123Sur , Medellin , Colombia",
            "phone": "+57 (305) 234-4567",
        })
        return context  
