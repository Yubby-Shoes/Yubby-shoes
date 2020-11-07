from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import (CreateView, ListView, DetailView, UpdateView,
                                  DeleteView)
from .forms import ProductInfoModelForm, OrderStatusUpdateForm
from .models import Product, Category, OrderItem
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from accounts.models import Customer


@method_decorator(login_required, name='dispatch')
class Create(CreateView):
    form_class = ProductInfoModelForm
    template_name = 'store/create.html'

    def get_success_url(self):
        return reverse('store:filter', args=['All'])


@method_decorator(login_required, name='dispatch')
class Detail(DetailView):
    template_name = 'store/detail.html'
    context_object_name = 'product'
    model = Product


@method_decorator(login_required, name='dispatch')
class Update(UpdateView):
    form_class = ProductInfoModelForm
    model = Product
    template_name = 'store/update.html'

    def get_success_url(self):
        return reverse('store:filter', args=['All'])


@method_decorator(login_required, name='dispatch')
class Delete(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('store:filter', args=['All'])


@login_required()
def filter_products_bycategory(request, category):
    if category == 'All' or category == 'all':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(
            category__category_name__contains=category)
    return render(request, 'store/list.html', context={
        'data': products,
        "category": Category.objects.all()
    })


@method_decorator(login_required, name='dispatch')
class Orders(ListView):
    template_name = 'store/order.html'
    model = OrderItem
    context_object_name = 'orders'

    def get_queryset(self):
        return self.model.objects.all().order_by('-ordered_on')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['update_form'] = OrderStatusUpdateForm()
        return data


@login_required()
@require_http_methods(["GET"])
def customers_view(request):
    customers = Customer.objects.all()
    # pn = request.GET.get('phone_number')

    # if pn:
    #     customers = get_object_or_404(Category, phone_number=pn)
    #     # print(products)

    return render(request, 'store/customer.html', context={
        'customers': customers,
        'shoe_sizes': [39, 40, 41, 42, 43]
    })


@login_required()
@require_http_methods(["POST"])
def customers_update(request, pk):
    customers = Customer.objects.all()
    # pn = request.GET.get('phone_number')

    # if pn:
    #     customers = get_object_or_404(Category, phone_number=pn)
    #     # print(products)

    return render(request, 'store/customer.html', context={
        'customers': customers,
        'sizes': [39, 40, 41, 42, 43]
    })


@method_decorator(login_required, name='dispatch')
class OrderStatusUpdateView(UpdateView):
    template_name = 'store/order.html'
    success_url = reverse_lazy('store:orders')
    form_class = OrderStatusUpdateForm

    def get_queryset(self):
        return OrderItem.objects.all()

    # def form_valid(self, form):
    #     print(self.object.product)
    #     print(self.object.product.in_stock)
    #     print(self.object.order_status)
    #     if self.object.product.in_stock > 0:
    #         if self.object.order_status == 'PR':
    #             self.object.product.in_stock -= self.object.order_quantity
    #
    #     return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #
    #     form = self.get_form()
    #     if form.is_valid():
    #         if self.object.product.in_stock > 0:
    #             if self.object.order_status == 'SH':
    #                 self.object.product.in_stock -= self.object.order_quantity
    #
    #                 self.object.product.save()
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)
