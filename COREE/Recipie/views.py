from django.shortcuts import render,redirect
from Recipie.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout 

# Create your views here.

def recipie(request):
    if request.method=='POST':
        data=request.POST

        name=data.get('name')
        description=data.get('description')
        steps=data.get('steps')
        image=request.FILES.get('image')

        recipie_model.objects.create(
            name=name,
            description=description,
            steps=steps,
            image=image
        )

        return redirect('recipie')
    
    querryset=recipie_model.objects.all()

    if request.GET.get('search'):
        querryset = querryset.filter(name__icontains=request.GET.get('search'))
    context={'recipies':querryset}
    
    return render(request, 'recipie.html',context)


def update_recipie(request,id):

    U_recipie = recipie_model.objects.get(id=id)

    if request.method=='POST':
        data=request.POST

        U_recipie.name=data.get('name')
        U_recipie.description=data.get('description')
        U_recipie.steps=data.get('steps')
        if request.FILES.get('image'):
         U_recipie.image = request.FILES.get('image')

        U_recipie.save()

        return redirect('recipie')
    
    context={'U_recipie':U_recipie,'recipies':recipie_model.objects.all()}
    
    return render(request,'recipie.html',context)


def delete_recipie(request,id):

    querryset = recipie_model.objects.get(id=id)
    querryset.delete()

    return redirect('/')


def login_page(request):

    if request.method=='POST':
        data=request.POST

        username=data.get('username')
        password=data.get('password')

        
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username')
            return redirect('login_page')
        
        user = authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid password')
            return redirect('login_page')
        
        login(request,user)
        return redirect('recipie')


    return render(request,'login.html')


def register_page(request):

    if request.method=='POST':
        data=request.POST

        first_name=data.get('firstname')
        last_name=data.get('lastname')
        username=data.get('username')
        password=data.get('password')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'username already taken')
            return redirect('register_page')

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)
        user.save()

        messages.info(request,'account created sucessfully')

        return redirect('register_page')



    return render(request,'register.html')

def logout_page(request):

    logout(request)
    return redirect('login_page')

