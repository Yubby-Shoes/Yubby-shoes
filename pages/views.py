from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from django.core.paginator import Paginator
from store.models import *


def index(request):
    if request.method == 'GET':
        # to return just 9 latest products
        products = Product.objects.all().order_by('-date_added')[:9]
        # print('products=', len(products))
        context = {
            'products': products
        }
        return render(request, 'index.html', context=context)
    return HttpResponseNotAllowed('Methods Other than get not allowed!')


def shop(request):
    if request.method == 'GET':
        products = Product.objects.all()
        p = Paginator(products, 9)
        page_no = request.GET.get('page', 1)
        paginated_products = p.get_page(page_no)
        return render(request, 'shop.html', context={
            'products': paginated_products
        })
    return HttpResponseNotAllowed('Methods Other than get not allowed!')


def about(request):
    return render(request, 'about.html', context={})


def blog(request):
    return render(request, 'blog.html', context={})


def contact(request):
    return render(request, 'contact.html', context={})
