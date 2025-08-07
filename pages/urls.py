from django.urls import path
from .views import (
    CartView,
    HomePageView,
    AboutPageView,
    ContactPageView,
    ImageViewFactory,
    ProductIndexView,
    ProductShowView,
    ProductCreateView,
    CartRemoveAllView,
    ImageViewNoDI

)
from .utils import ImageLocalStorage


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/<str:id>/', ProductShowView.as_view(), name='show'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<int:product_id>/', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
    path('image-no-di/', ImageViewNoDI.as_view(), name='image_no_di'), 


]
