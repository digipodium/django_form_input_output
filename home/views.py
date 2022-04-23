from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import ProductForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def formview(request):
    ctx = {} # empty dict
    form = ProductForm() # create empty form
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES) # create form with POST data
        if form.is_valid():
            form.save()
            return redirect('listing')
    ctx['form'] = form
    return render(request, 'form.html', ctx)

def listingview(request):
    product_list = Product.objects.all()
    categories = Category.objects.all()
    ctx = {
        'p_list': product_list,
        'categories': categories,
    }
    return render(request, 'listing.html', ctx)

def detailview(request,id):
    product = get_object_or_404(Product, pk=id)
    ctx = {'product': product,}
    return render(request, 'detail.html', ctx)

def categoryview(request):
    filter = request.GET.get('c')
    if filter:
        products = Product.objects.filter(category__name=filter)
    else:
        return redirect('listing')

    ctx = {
        'p_list': products,
        'category': filter,
        'count': products.count(),
    }
    return render(request, 'category.html', ctx)