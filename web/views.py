from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProductForm,CustomerForm
from .models import Product,Customer
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('app:view_home')
        else:
            messages.error(request,'USUARIO NO VALIDO')
            return  redirect('app:view_login')
        
        return render(request,'auth/login.html')
    
    else:
        return render(request,'auth/login.html')
    
def view_logout(request):
    logout(request)
    return redirect('app:view_login') 


def view_register(request):
    return render(request,'auth/register.html')

def view_home(request):
    return render(request,'views/home.html')

def view_sale(request):
    return render(request,'aplication/sale.html')

#  app inventory.
def view_inventory(request):
    if request.method == 'POST':
        producto = request.POST['product']
        search_products = Product.objects.filter(name__startswith = producto)
        return render(request,'aplication/inventory.html',{'products':search_products})
    
    else:
        products = Product.objects.all()
        paginator = Paginator(products,4)
        page = request.GET.get('page',1)
        products_page = paginator.page(page)
        return render(request,'aplication/inventory.html',{'products':products_page})
    
def view_inventory_delete(request,id):
    delete_product = get_object_or_404(Product,pk=id)
    delete_product.delete()
    return redirect('app:view_inventory')    

def view_inventory_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            stock = form.cleaned_data['stock']
            Product.objects.create(name=name,description=description,price=price,stock=stock,user_id=request.user.id)

            return redirect('app:view_inventory')
    else:
        form = ProductForm()
    return render(request,'forms/inv_form.html',{'form':form})   


#  app customer.

def view_customer(request):

    customers = Customer.objects.all()
    print("customer")
    return render(request,'aplication/customer.html',{'customers':customers})

def view_customer_form(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            Customer.objects.create(
                name=name,
                last_name=last_name,
                age=age,
                email=email,
                phone=phone,
                user_id=request.user.id)
            return redirect('app:view_customer')
    else:
        form = CustomerForm()
    return render(request,'forms/customer_form.html',{'form':form})   



