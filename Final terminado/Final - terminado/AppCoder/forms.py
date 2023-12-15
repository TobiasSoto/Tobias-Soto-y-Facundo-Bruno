from django import forms
from .models import Curso, Avatar
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormularioCurso(forms.Form):

    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class FormularioEstudiante(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class FormularioLibros1(forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    numerodeguardado = forms.IntegerField()

class FormularioProfesor(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    porfesion = forms.CharField(max_length=40)


class RegisterFormulario(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ["email","first_name","last_name", "password1" , "password2"]
    
    def clean_password2(self):

        self.cleaned_data
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        
        if password1 != password2:
            raise forms.ValidationError("Deben coincidir ambas contraseñas")
        return password2

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ("imagen",)