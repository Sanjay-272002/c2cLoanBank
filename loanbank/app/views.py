from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import UserForm
from .models import UserModel
import random

# Create 
def create(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Request for loan')
            return redirect('read')

    context = { 'form':form }
    return render(request, 'app/create.html', context)

# Read
def read(request):
    user_data = UserModel.objects.all()
    context = { 'user_data': user_data }
    return render(request, 'app/read.html', context)

# Update
def update(request, pk):
    get_user_data = get_object_or_404(UserModel, pk=pk)
    form = UserForm(instance=get_user_data)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=get_user_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated')
            return redirect('read')

    context = { 'form':form }
    return render(request, 'app/update.html', context)

# Delete
def delete(request, pk):
    get_user = get_object_or_404(UserModel, pk=pk)
    get_user.delete()
    messages.error(request, 'Loan request decline')
    return redirect('/')

def calculateCibilScore(request):
    cibil_scrore =  random.randint(300, 700);
    if cibil_scrore:
     return render(request, 'app/read.html',cibil_scrore)
    else: 
     return render(request, 'app/read.html','')
