
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('about/', views.about, name='AboutUs'),
    path('product/<int:myid>', views.productView, name='ProductView'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracking/', views.tracker, name='OrderTracking'),
    path('search/', views.search, name='Search'),
    path('checkout/', views.checkout, name='CheckOut'),
    path('handlerequest/', views.handlerequest, name='handlerequest'),
]
