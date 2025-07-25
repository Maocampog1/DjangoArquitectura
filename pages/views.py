
# Create your views here.
from django.shortcuts import render # here by default
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.shortcuts import redirect

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
#Activity 1
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
    

class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV", "price": 599.99},
        {"id": "2", "name": "iPhone", "description": "Best iPhone", "price": 999.99},
        {"id": "3", "name": "Chromecast", "description": "Best Chromecast", "price": 49.99},
        {"id": "4", "name": "Glasses", "description": "Best Glasses", "price": 19.99},
    ]
    

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        viewData = {}

        try:
            # Convertir el id a entero (puede fallar si no es número)
            product_index = int(id) - 1

            # Verificar que el índice esté dentro de la lista de productos
            if product_index < 0 or product_index >= len(Product.products):
                # Si está fuera de rango, redirigir al home
                return HttpResponseRedirect(reverse('home'))

        except ValueError:
            # Si el id no es número (ejemplo: abc), redirigir al home
            return HttpResponseRedirect(reverse('home'))

        # Si es válido, obtener el producto
        product = Product.products[product_index]
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product
        return render(request, self.template_name, viewData)

#Actividad 7
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    # Validación personalizada para el campo price
    def clean_price(self):
        price = self.cleaned_data.get('price')

        # Verifica que sea mayor que 0
        if price is not None and price <= 0:
            raise forms.ValidationError("The price must be greater than 0.")

        return price
    

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {
            "title": "Create product",
            "form": form
        }
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            # Pasamos created=True para mostrar el mensaje en la plantilla
            viewData = {
                "title": "Create product",
                "form": ProductForm(),  # formulario vacío luego de crear
                "created": True
            }
            return render(request, self.template_name, viewData)
        else:
            viewData = {
                "title": "Create product",
                "form": form
            }
            return render(request, self.template_name, viewData)
