from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import widgets

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not CustomUser.objects.filter(email = email).exists():
            self.add_error('email','bu mail adresi kayıtlı değil')
        return email




class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username','email','birth_date','phone')
        # fields = '__all__'
    

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['last_name'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['username'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class':'form-control'})
        self.fields['birth_date'].widget = widgets.DateInput(attrs={'class':'form-control','type':'date'})
        self.fields['phone'].widget = widgets.TextInput(attrs={'class':'form-control'})


        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class':'form-control'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class':'form-control'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email = email).exists():
            self.add_error('email','bu mail adresi zaten kullanılıyor')
        return email
    


class CreateProfil(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ('title','image')
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['image'].widget = widgets.FileInput(attrs={'class':'form-control'})