from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




from .models import TASKS,FULFILLED


class TASKSForm(ModelForm):
	class Meta:
		model = TASKS
		fields = '__all__'
            
class CreateUserForm(UserCreationForm):
    	class Meta:
		       model = User
		       fields = ['username', 'email', 'password1', 'password2']	

class FULFILLEDForm(ModelForm):   	
        class Meta:
              model = FULFILLED
              fields = '__all__'
              exclude = ['Whse_Mangament']

