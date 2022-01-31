from django.core import paginator
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.views import View
from django.views import View


# Create your views here.

def index(request):
    dict = {}

    return render(request, 'Coffee_App/index.html', context=dict)


def blog(request):
    dict = {}

    return render(request, 'Coffee_App/blog.html', context=dict)


def about(request):
    dict = {}

    return render(request, 'Coffee_App/about.html', context=dict)


def blog_single(request):
    dict = {}

    return render(request, 'Coffee_App/blog_single.html', context=dict)


def cart(request):
    dict = {}

    return render(request, 'Coffee_App/cart.html', context=dict)


def checkout(request):
    dict = {}

    return render(request, 'Coffee_App/checkout.html', context=dict)


def contact(request):
    dict = {}

    return render(request, 'Coffee_App/contact.html', context=dict)


def menu(request):
    dict = {}

    return render(request, 'Coffee_App/menu.html', context=dict)


def product_single(request):
    dict = {}

    return render(request, 'Coffee_App/product_single.html', context=dict)


def service(request):
    dict = {}

    return render(request, 'Coffee_App/services.html', context=dict)


def shop(request):
    dict = {}

    return render(request, 'Coffee_App/shop.html', context=dict)
