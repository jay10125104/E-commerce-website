from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Customer, Product, Cart, OrderPlaced
from django.contrib import messages
from django.contrib.auth import logout
import time
def login(request):
    return render(request, 'app/login.html')
def logoutuser(request):
    logout(request)
    return redirect('login')
def passwordchaged(request):
    logoutuser(request)
    return render(request, 'app/passwordchanged.html')

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        # print(form)
        context = {'form': form}
        return render(request, 'app/customerregistration.html', context)

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'congratulation!register successfully')
            form.save()
        context = {'form': form}
        return render(request, 'app/customerregistration.html', context)
        # return render(request, template_name)
@login_required(login_url='login')
def home(request):
    topwears = Product.objects.filter(category='TW')
    bottomwears = Product.objects.filter(category='BW')
    mobiles = Product.objects.filter(category='M')
    laptop = Product.objects.filter(category='L')
    context = {'topwears': topwears, 'bottomwears': bottomwears,
               'laptop': laptop, 'mobiles': mobiles}
    return render(request, 'app/home.html', context)
@login_required(login_url='login')
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'app/productdetail.html', {'product': product})
@login_required(login_url='login')
def add_to_cart(request):
    return render(request, 'app/addtocart.html')
@login_required(login_url='login')
def buy_now(request):
    return render(request, 'app/buynow.html')
@login_required(login_url='login')
def profile(request):
    return render(request, 'app/profile.html')
@login_required(login_url='login')
def address(request):
    return render(request, 'app/address.html')
@login_required(login_url='login')
def orders(request):
    return render(request, 'app/orders.html')
@login_required(login_url='login')
def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'vivo' or data == 'samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(
            category='M').filter(discounted_price__lt=5000)
    else:
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    return render(request, 'app/mobile.html', {'mobiles': mobiles})
@login_required(login_url='login')
def laptop(request, data=None):
    if data == None:
        laptops = Product.objects.filter(category='L')
    elif data == 'lenovo' or data == 'tuff':
        laptops = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'below':
        laptops = Product.objects.filter(
            category='L').filter(discounted_price__lt=35000)
    else:
        laptops = Product.objects.filter(category='L').filter(brand=data)
    return render(request, 'app/laptop.html', {'laptops': laptops})
@login_required(login_url='login')
def checkout(request):
    return render(request, 'app/checkout.html')
        
