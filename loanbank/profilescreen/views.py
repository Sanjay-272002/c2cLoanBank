from multiprocessing import context
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .forms import dataForm
from .models import data
# from .forms import Profile_Form
# from .models import User_Profile

# IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

# Create your views here.
# def profilescreens(request):
#     form = Profile_Form()
#     if request.method == 'POST':
#         form = Profile_Form(request.POST, request.FILES)
#         if form.is_valid():
#             user_pr = form.save(commit=False)
#             user_pr.aadharcard = request.FILES['aadharcard']
#             file_type = user_pr.aadharcard.url.split('.')[-1]
#             file_type = file_type.lower()

#             user_pr.pancard = request.FILES['pancard']
#             file_type = user_pr.pancard.url.split('.')[-1]
#             file_type = file_type.lower()

#             user_pr.salaryslips = request.FILES['salaryslips']
#             file_type = user_pr.salaryslips.url.split('.')[-1]
#             file_type = file_type.lower()

#             user_pr.photo = request.FILES['photo']
#             file_type = user_pr.photo.url.split('.')[-1]
#             file_type = file_type.lower()

#             if file_type not in IMAGE_FILE_TYPES:
#               return render(request, 'profilescreen/error.html')
#             user_pr.save()
#         return render(request, 'profilescreen/details.html', {'user_pr': user_pr})
#     context = {"form": form,}
#     return render(request, 'profilescreen/create.html', context)

# def upload(request):
#     context= {}
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         fs = FileSystemStorage()
#         name=fs.save(uploaded_file.name, uploaded_file)
#         context['url'] = fs.url(name)

#     return render(request,'upload.html',context)

def data_list(request):
    datas= data.objects.all()
    return render(request,'data_list.html',{ 'datas':datas })

def upload_data(request):
    if request.method == 'POST':
       form = dataForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('home') 
    else:
            form = dataForm()
    return render(request,'upload_data.html',{ 'form':form})
    
        