from django.shortcuts import render
from .models import Product
from .forms import RangeFilterForm

def product_list(request):
    products = Product.objects.all()
    form = RangeFilterForm(request.GET)
    
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        size = form.cleaned_data.get('size')
        
        if min_price is not None:
            products = products.filter(price__gte=min_price)
        if max_price is not None:
            products = products.filter(price__lte=max_price)
        if size:
            products = products.filter(size=size)
    
    return render(request, 'products/product_list.html', {'products': products, 'form': form})

from django.http import HttpResponse

def populate_products(request):
    sizes = ['Small', 'Medium', 'Large']

    for i in range(1, 21):
        Product.objects.create(
            name=f"Product {i}",
            price=25 * i,
            size=sizes[i % 3]
        )
    return HttpResponse("20 product entries added successfully!")
