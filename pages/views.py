from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

from .models import Product

# Página principal
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

# About
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

# Contact
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

# Mostrar producto
class ProductShowView(View):
    template_name = 'products/index.html'

    def get(self, request, id):
        try:
            product_id = int(id)
            if product_id < 1:
                raise ValueError("Product ID must be 1 or greater")
        except (ValueError, TypeError):
            return HttpResponseRedirect(reverse('home'))

        product = get_object_or_404(Product, pk=product_id)

        context = {
            "title": f"{product.name} - Online Store",
            "subtitle": f"{product.name} - Product information",
            "product": product,
        }
        return render(request, self.template_name, context)

# Listar productos
class ProductIndexView(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Products - Online Store'
        context['subtitle'] = 'List of products'
        return context

# Formulario
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("The price must be greater than 0.")
        return price

# Crear producto
class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name, {"title": "Create product", "form": form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data["name"],
                price=form.cleaned_data["price"]
            )
            return render(request, self.template_name, {
                "title": "Create product",
                "form": ProductForm(),
                "created": True
            })
        return render(request, self.template_name, {
            "title": "Create product",
            "form": form
        })
    
