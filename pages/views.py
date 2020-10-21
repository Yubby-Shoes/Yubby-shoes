from random import randint
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotAllowed, Http404
from django.core.paginator import Paginator
from store.models import *


def get_categories():
    """
    :return: QuerySet of all the categories present.
    """
    return Category.objects.all()


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
        products = Product.objects.all().order_by('-date_added')
        p = Paginator(products, 9)
        page_no = request.GET.get('page', 1)
        paginated_products = p.get_page(page_no)
        return render(request, 'shop.html', context={
            'products': paginated_products,
            'categories': get_categories()
        })
    return HttpResponseNotAllowed('Methods Other than get not allowed!')


def item_detail(request, pk):
    if request.method == 'GET':
        item = get_object_or_404(Product, pk=pk)
        products = Product.objects.all()
        start_item = randint(1, len(products)-3)
        # print('start_item', start_item)
        context = {
            'product': item,
            'featured_products': products[start_item: start_item+3],
            'categories': get_categories()
        }
        return render(request, 'shop-single.html', context=context)
    return HttpResponseNotAllowed('Methods Other than get not allowed!')


def about(request):
    return render(request, 'about.html', context={})


def blog(request):
    return render(request, 'blog.html', context={})


def contact(request):
    return render(request, 'contact.html', context={})
