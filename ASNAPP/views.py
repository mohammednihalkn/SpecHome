from .models import *
from django.shortcuts import render, redirect
def home(request):
    return render(request, 'home.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = ASN.objects.get(name=username, password=password)
        request.session['user_id'] = user.id
        return redirect('userhome')  # Redirect to home page after successful login
    return render(request, 'Login.html')  

def Register(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password') 
        user = ASN.objects.create(name=username, password=password)
        user.save()
        request.session['user_id'] = user.id
        return redirect('Login')  # Redirect to login page after successful registration
    return render(request, 'register.html') 

def userhome(request):
    return render(request, 'userhome.html') 

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        admin = Admin.objects.get(username=username, password=password)
        request.session['admin_id'] = admin.id
        return redirect('adminhome')  # Redirect to admin home page after successful login
    return render(request, 'adminlogin.html') 
  
def adminhome(request):
    return render(request, 'adminhome.html')

def adminac(request):
      if request.method == 'POST':
        name = request.POST.get('name')
        user = company.objects.create(name=name)
        user.save()
        return redirect('adminac')

      a=company.objects.all()
      return render(request, 'adminac.html',{'a':a})

def add_product(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        com=company.objects.get(id=id)
        user = product.objects.create(name=name, com=com)
        user.save()
        return redirect('add_product', id=id)

    a=product.objects.filter(com=id)
    return render(request, 'add_product.html', {'a': a})

def add_specifications(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        prod=product.objects.get(id=id)
        user = specifications.objects.create(name=name, prod=prod)
        user.save()
        return redirect('add_specifications', id=id)

    a=specifications.objects.filter(prod=id)
    return render(request, 'add_specifications.html', {'a': a})

def userviewcompany(request):
    a=company.objects.all()
    return render(request, 'userviewcompany.html',{'a':a})

def userviewmodel(request, id):
    a = product.objects.filter(com_id=id)
    return render(request, 'userviewmodel.html', {'a': a})

def userviewspecification(request, id):
    a=specifications.objects.filter(prod=id)
    return render(request, 'userviewspecification.html',{'a':a})

def delete_company(request, id):
    company.objects.get(id=id).delete()
    return redirect('adminac')


def delete_product(request, id):
    p = product.objects.get(id=id)
    company_id = p.com.id

    p.delete()

    return redirect('add_product', id=company_id)


def delete_specification(request, id):
    spec = specifications.objects.get(id=id)
    product_id = spec.prod.id

    spec.delete()

    return redirect('add_specifications', id=product_id)

def logout(request):
    request.session.flush()
    return redirect('home')
