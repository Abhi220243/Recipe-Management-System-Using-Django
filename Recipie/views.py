from django.shortcuts import render,redirect
from Recipie.models import *

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

        return redirect('/')
    
    querryset=recipie_model.objects.all()
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

        return redirect('/')
    
    context={'U_recipie':U_recipie,'recipies':recipie_model.objects.all()}
    
    return render(request,'recipie.html',context)


def delete_recipie(request,id):

    querryset = recipie_model.objects.get(id=id)
    querryset.delete()

    return redirect('/')