from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import Member
from .forms import RegisterForm
from django.contrib.auth.hashers  import make_password, check_password 
from django.contrib.auth import login,logout

# Create your views here.


def homeView(request):
	return render(request,'index.html')


def dashboardView(request):
	student = Member.objects.get(request.session['member_id'])
	return render(request,'dashboard.html')

def librarianView(request):
	librarian = Member.objects.get(request.session['member_id'])
	return render(request,'librarian.html')

def registerView(request):
	if request.method =='POST' :
		form = RegisterForm(request.POST)
		if form.is_valid() :
			username = request.POST['username']
			email	 = request.POST['email']
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			is_student = request.POST['is_student']
			password = make_password(request.POST['password'], salt=None, hasher='default')
			
			user = Member(username=username,password=password,first_name=first_name,last_name=last_name,email=email,is_student=is_student)
			user.save()

			login(request,user)
			request.session['member_id']= user.id

			if is_student:
				return HttpResponseRedirect('student/dashboard')
			else:
				return HttpResponseRedirect('library/dashboard')
	else:
		form=RegisterForm()

	context = {
			'form' : form
	}

	return render(request,'register.html',context)