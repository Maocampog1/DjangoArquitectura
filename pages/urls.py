from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    ProductIndexView,
    ProductShowView
)

urlpatterns = [
    # Página de inicio
    path('', HomePageView.as_view(), name='home'),

    # About y Contact
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    # Productos
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/<str:id>/', ProductShowView.as_view(), name='show'),
]
