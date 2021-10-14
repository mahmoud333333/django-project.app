from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import TASKSForm,CreateUserForm,FULFILLEDForm
from .filters import TASKSFilter
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


@unauthenticated_user
def registerPage(request):
    if request.user.is_authenticated:
            return redirect('home') 
    else:

            form = CreateUserForm()
            if request.method == 'POST':
                    form = CreateUserForm(request.POST)
                    if form.is_valid():
                            form.save()
                            user = form.cleaned_data.get('username')

                            group = Group.objects.get(name='customer')
                            user.groups.add(group)
                            GMANAGER.objects.create(
				               user=user,
				               name=user.username,
                                )
                            
                            messages.success(request, 'Account was created for ' + username)

                            return redirect('login')
			

    context = {'form':form}
    return render(request, 'product/register.html', context)
@unauthenticated_user
def loginPage(request):
	
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'product/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    tasks = TASKS.objects.all()
    staff=STAFF.objects.all()
    total_staff=staff.count()
    myFilter = TASKSFilter(request.GET, queryset=tasks)
    tasks= myFilter.qs
    total_tasks = tasks.count()
    accepted = tasks.filter(status='Accepted').count()
    pending = tasks.filter(status='Pending').count()

    context = {'tasks':tasks, 'staff':staff,
	'total_tasks':total_tasks,'Accepted':accepted,
	'pending':pending,'item':tasks,'myFilter':myFilter}
    
    return render(request,'product/dashboard.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
     
     staff=STAFF.objects.get(user=request.user)
     tasks = staff.tasks_set.all()
     myFilter = TASKSFilter(request.GET, queryset=tasks)
     tasks= myFilter.qs
     total_tasks=tasks.count()
     accepted = tasks.filter(status='accepted').count()
     pending = tasks.filter(status='Pending').count()

     context = {'tasks':tasks, 'total_tasks':total_tasks,
    'pending':pending,'myFilter':myFilter} 
     return render(request, 'product/user.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def whse(request):
    global whse    
    whse = Whse_Mangament.objects.all()
    return render(request,'product/whse.html',{'whse':whse})
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def staff(request, pk_test):
    staff=STAFF.objects.get(id=pk_test)

    tasks = staff.taska_set.all()
    tasks_count = tasks.count()

    myFilter = TASKSFilter(request.GET, queryset=tasks)
    tasks= myFilter.qs

    context={'staff':STAFF, 'tasks':tasks,'tasks_count':tasks_count,'myFilter':myFilter}
    return render(request,'product/staff.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createTASKS(request):
    form = TASKSForm()
    if request.method == 'POST':
        subject='NEW TASK '
        message ='you recieved NEW TASK '
        from_email=settings.EMAIL_HOST_USER
        recipient_list=['teamwhse@gmail.com']
        send_mail(subject,message, from_email,recipient_list,fail_silently=True)
	       	#print('Printing POST:', request.POST)
        form = TASKSForm(request.POST,request.FILES)
            
        if form.is_valid():
		       form.save()

            
        return redirect('/')


    context = {'form':form}
    
    return render(request, 'product/TASKS_form.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateTASKS(request, pk):
    
    tasks = TASKS.objects.get(id=pk)
    form = TASKSForm(instance=tasks)
    
    if request.method == 'POST':
        subject='NEW TASK'
        message ='you recieved NEW TASK '
        from_email=settings.EMAIL_HOST_USER
        recipient_list=['teamwhse@gmail.com']
        send_mail(subject,message, from_email,recipient_list,fail_silently=True)
        form = TASKSForm(request.POST,request.FILES, instance=tasks)
        if form.is_valid():
           form.save()
           
            
           return redirect('/')
          
    context = {'form':form}
       
    return render(request, 'product/tasks_form.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteTASKS(request, pk):
    
	tasks = TASKS.objects.get(id=pk)
	if request.method == "POST":
		    tasks.delete()
		    return redirect('/')

	context = {'item':tasks}
	return render(request, 'product/delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def confirmedTASKS(request,pk):
    tasks = TASKS.objects.get(id=pk)
    form = FULFILLEDForm(instance=tasks)
    if request.method == 'POST':
        subject='DONE'
        message ='there is update on the tasks '
        from_email=settings.EMAIL_HOST_USER
        recipient_list=['teamwhse@gmail.com']
        send_mail(subject,message, from_email,recipient_list,fail_silently=True)
        form =FULFILLEDForm(request.POST,request.FILES)
        if form.is_valid():
           form.save()
           return redirect('/')

    context = {'form':form}
    return render(request, 'product/Confirmed_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def Status(request):
      
   status = FULFILLED.objects.all()
   myFilter = TASKSFilter(request.GET, queryset=status)
   status= myFilter.qs
   context={'status':status,'myFilter':myFilter}
   return render(request,'product/statuspage.html',context)
   


        


        

