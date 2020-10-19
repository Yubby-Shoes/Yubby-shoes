from django.shortcuts import render


def store(request):
    context = {}
    return render(request, 'store/store.html', context)


def buy(request):
    context = {}
    return render(request, 'store/buy.html', context)
