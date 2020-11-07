from django import forms
from django.forms import ModelForm
from .models import Member


class RegisterForm(ModelForm):
	class Meta:
		model = Member
		fields = ['username','email','first_name','last_name','is_student','password']

	password = forms.CharField(
    	widget=forms.PasswordInput()
	)
	
	

	def clean_username(self):
		username = self.cleaned_data['username']

		try:
			user = Member.objects.get(username=username)
		except:
			return username
		raise forms.ValidationError(u'Username "%s" is already in use.' % username)

	def clean_email(self):
		email = self.cleaned_data['email']

		try:
			email= Member.objects.get(email=email)
		except:
			return email
		raise forms.ValidationError('email already registered')

