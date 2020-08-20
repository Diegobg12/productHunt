from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone


# Create your views here.


def home(request):
    products = Product.objects
    return render(request, 'products/home-copy.html', {'products':products})

def about(request):
    return render(request, 'products/about.html')

def catView(request):
    category = get_object_or_404(category, category=category_id).all()
    projectsCat = get_object_or_404(Product, category=category_id).all()
    return render(request, 'products/catView.html', {'projectsCat':projectsCat, category:'category'})

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.image = request.FILES['image']
            product.icon = request.FILES['icon']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.save()
            return redirect('/products/' + str(product.id) ) 

        else :
            return render(request, 'products/create.html', {'error':'All fields are required.'})

    
    else:
        return render(request, 'products/create.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/single.html', {'product':product})

@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))
