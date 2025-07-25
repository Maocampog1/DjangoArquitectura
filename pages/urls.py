from django.urls import path
from .views import homePageView

urlpatterns = [

    # Define the URL pattern for the home page
    path("", homePageView, name='home')

]
