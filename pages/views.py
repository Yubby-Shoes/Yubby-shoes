from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', context={})


def shop(request):
    return render(request, 'shop.html', context={})


def about(request):
    return render(request, 'about.html', context={})


def blog(request):
    return render(request, 'blog.html', context={})


def contact(request):
    return render(request, 'contact.html', context={})
