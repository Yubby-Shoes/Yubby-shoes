from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import ProductInfoModelForm
from .models import Product

# @login_required()
# def products_view(request):
#     # this context is passed for statusapp
#     # messages = StatusMessage.objects.filter(user=request.user)
#     products = Product.objects.all()
#     return render(request, 'store/store.html', {
#         'products': products
#     })


class List(ListView):
    template_name = 'store/list.html'
    model = Product
    context_object_name = 'data'


class Create(CreateView):
    form_class = ProductInfoModelForm
    template_name = 'store/create.html'

    def get_success_url(self):
        return reverse('store:list')


class Detail(DetailView):
    template_name = 'store/detail.html'
    context_object_name = 'user_obj'
    model = Product


class Update(UpdateView):
    form_class = ProductInfoModelForm
    model = Product
    template_name = 'store/update.html'

    def get_success_url(self):
        return reverse('store:list')


class Delete(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('store:list')
