from random import randint
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotAllowed, Http404
from django.core.paginator import Paginator
from store.models import *
from .forms import UserDetailForm


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
            'products': products,
            'categories': get_categories()
        }
        return render(request, 'pages/index.html', context=context)
    return HttpResponseNotAllowed('Methods Other than get not allowed!')


def shop(request):
    if request.method == 'GET':
        products = Product.objects.filter(
            category__category_name__startswith="men").order_by('-date_added')
        cg = request.GET.get('category')

        if cg:
            category = get_object_or_404(Category, pk=cg)
            products = category.product_set.all().order_by('-date_added')
            # print(products)

        p = Paginator(products, 9)
        page_no = request.GET.get('page', 1)
        paginated_products = p.get_page(page_no)
        return render(request, 'pages/shop.html', context={
            'products': paginated_products,
            'categories': Category.objects.filter(category_name__startswith="men")
        })
    return HttpResponseNotAllowed('Methods Other than get not allowed!')


def shop_women(request):
    if request.method == 'GET':
        products = Product.objects.filter(
            category__category_name__startswith="women").order_by('-date_added')
        cg = request.GET.get('category')

        if cg:
            category = get_object_or_404(Category, pk=cg)
            products = category.product_set.all().order_by('-date_added')
            # print(products)

        p = Paginator(products, 9, allow_empty_first_page=True)
        page_no = request.GET.get('page', 1)
        print(page_no)
        paginated_products = p.get_page(page_no)
        # print(paginated_products.previous_page_number())
        return render(request, 'pages/shop.html', context={
            'products': paginated_products,
            'categories': Category.objects.filter(category_name__startswith="women")
        })
    return HttpResponseNotAllowed('Methods Other than get not allowed!')


def item_detail(request, pk):
    if request.method == 'GET':
        item = get_object_or_404(Product, pk=pk)
        products = Product.objects.all()
        if len(products) > 4:
            start_item = randint(1, len(products)-3)
            featured_products = products[start_item: start_item+3]
        else:
            featured_products = products
        # print('start_item', start_item)
        context = {
            'product': item,
            'featured_products': featured_products,
            'categories': get_categories()
        }
        return render(request, 'pages/shop-single.html', context=context)
    return HttpResponseNotAllowed('Methods Other than get not allowed!')


def about(request):
    return render(request, 'pages/about.html', context={})


def buy(request, pk):
    buy_detail_form = UserDetailForm()
    product = get_object_or_404(Product, pk=pk)
    # print(product)
    if request.method == 'POST':
        buy_detail_form = UserDetailForm(request.POST)
        if buy_detail_form.is_valid():
            buy_detail_form.save(pk)
            buy_detail_form = UserDetailForm()
    return render(request, 'pages/buy.html', context={
        'buy_detail_form': buy_detail_form,
        'product': product
    })


def contact(request):
    return render(request, 'pages/contact.html', context={})
