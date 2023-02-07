from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth.decorators import login_required



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import CreateUserForm




from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def registerpage(request):
	if request.user.is_authenticated:
		return redirect('index')

	else:
			form = CreateUserForm()
			if request.method == 'POST':
				form = CreateUserForm(request.POST)
				if form.is_valid():
					form.save()
					user = form.cleaned_data.get('username')
					messages.success(request, 'Account was created for' + user)
					return render(request, '/Users/hysntechnologies/Desktop/sales/natty/data/templates/login.html')





			context = {'form':form}
			return render(request, '/Users/hysntechnologies/Desktop/sales/natty/data/templates/register.html', context)

def loginpage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
			if request.method == 'POST':
				username = request.POST.get('username')
				password = request.POST.get('password')
				user = authenticate(request ,username=username, password = password)

				if user is not None:
					login(request ,user)
					return redirect('index')
				else:
					messages.info(request, 'Username or Password is incorrect')



			context = {}
			return render(request, 'login.html', context)



def logoutUser(request):
	logout(request)
	messages.info(request, 'you have logout successfully')
	return redirect('login')

@login_required(login_url='login')






def index(request):
    return render(request, 'index.html')
@login_required(login_url='login')

def index(request):
    members_list = Mastersheet.objects.all()
    Leadfedders = Leadfedder.objects.all()
    sub = Retail_Count.objects.all()
    ret = Retail.objects.all()
    Fin= Financial.objects.all()
    paginator = Paginator(members_list, 50000)
    page = request.GET.get('page')
    paginator1 = Paginator(sub, 50000)
    page1 = request.GET.get('page')
    paginator2 = Paginator(ret, 50000)
    page2 = request.GET.get('page')
    paginator3 = Paginator(Leadfedders, 50000)
    page3 = request.GET.get('page')
    paginator4 = Paginator(Fin, 50000)
    page4 = request.GET.get('page')
    total_companies = Mastersheet.objects.values('companiesname').distinct().count()
    total_data = members_list.count()
    total_data2 = Count.objects.values('companiesname').distinct().count()
    total_data3 = Leadfedders.count()
    total_data4 = ret.count()
    total_data5 = Fin.count()
    

    natty = total_companies
    natty1 = total_data
    natty2 = total_data2
    natty3 = total_data3
    natty4 = total_data4
    natty5 = total_data5
    
    

    

    try:
        Mastersheets = paginator.page(page)
        Mastersheets1 = paginator1.page(page1)
        Mastersheets2 = paginator2.page(page2)
        Mastersheets3 = paginator3.page(page3)
        Mastersheets4 = paginator4.page(page4)
    except PageNotAnInteger:
        Mastersheets = paginator.page(1)
        Mastersheets1 = paginator1.page(1)
        Mastersheets2 = paginator2.page(1)
        Mastersheets3 = paginator3.page(1)
        Mastersheets4 = paginator4.page(1)
    except EmptyPage:
        Mastersheets = paginator.page(paginator.num_pages)
        Mastersheets1 = paginator1.page(paginator1.num_pages)
        Mastersheets2 = paginator1.page(paginator2.num_pages)
        Mastersheets3 = paginator1.page(paginator3.num_pages)
        Mastersheets4 = paginator1.page(paginator4.num_pages)
    
    return render(request, 'index.html', {'Mastersheets': Mastersheets,'Mastersheets1': Mastersheets1,'Mastersheets2': Mastersheets2,'Mastersheets3': Mastersheets3,'Mastersheets4': Mastersheets4,'total_companies': natty,'total_data': natty1,'total_data2': natty2,'total_data3': natty3,'total_data4': natty4,'total_data5': natty5,})

