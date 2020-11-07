from django.shortcuts import render, reverse, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.urls import reverse_lazy
from django.views.generic import (CreateView, ListView, DetailView, UpdateView,
                                  DeleteView)
from .forms import ProductInfoModelForm, OrderStatusUpdateForm
from .models import Product, Category, OrderItem
from accounts.models import Customer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
        return self.model.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['update_form'] = OrderStatusUpdateForm()
        return data


@login_required
@require_http_methods(["GET"])
def CustomersView(request):
    phone_number = request.GET.get('phone_number')
    customers = Customer.objects.all()
    if phone_number:
        customers = get_object_or_404(Customers, phone_number=phone_number)
    return render(request, 'store/customers.html', context={
        'customers': customers
    })

# @method_decorator(login_required, name='dispatch')
# def customers_update_view(request):


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
