from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import Member,IssueRequest,Book

from django.contrib.auth.hashers  import make_password, check_password 
from django.contrib.auth import login,logout

# Create your views here.


def homeView(request):
	books= Book.objects.filter(status='Available')
	return render(request,'index.html',{'books':books})


def dashboardView(request):
	student = Member.objects.get(pk=request.session['member_id'])
	books = IssueRequest.objects.filter(member=student)
	context = {
		'books':books,
		'student':student
	}

	return render(request,'dashboard.html',context)

def librarianView(request):
	librarian = Member.objects.get(pk=request.session['member_id'])
	return render(request,'librarian.html')

def registerView(request):
	if request.method =='POST' :		
		username = request.POST.get('username')
		email	 = request.POST.get('email')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		member_type = request.POST.get('member_type')
		password = make_password(request.POST.get('password'), salt=None, hasher='default')
		user = Member(username=username,password=password,first_name=first_name,last_name=last_name,email=email,member_type=member_type)
		user.save()
		print(request.POST)

		login(request,user)
		request.session['member_id']= user.id

		if member_type=='student':
			return HttpResponseRedirect('student/dashboard')
		else:
			return HttpResponseRedirect('library/dashboard')
	
	return render(request,'register.html')






