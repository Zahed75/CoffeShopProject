from django.urls import include, re_path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    path('product_single/', views.product_single, name='product_single'),
    path('services/', views.service, name='services'),
    path('shop/', views.shop, name='shop'),
    path('cart/',views.cart,name='cart')

]
