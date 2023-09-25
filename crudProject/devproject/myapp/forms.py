from django import forms  
from myapp.models import Employee  



class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = ['firstname', 'lastname','contact', 'country', 'email', 'city'] 
        widgets = { 'firstname': forms.TextInput(attrs={ 'class': 'form-control' }),
            'lastname': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
            'country': forms.TextInput(attrs={ 'class': 'form-control' }),
            'city': forms.TextInput(attrs={ 'class': 'form-control' }),

            
      }