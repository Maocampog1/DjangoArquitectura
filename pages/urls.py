from django.urls import path
from .views import homePageView, AboutPageView  # Importa también AboutPageView

urlpatterns = [
    path("", homePageView, name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
