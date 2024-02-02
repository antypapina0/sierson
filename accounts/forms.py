from django import forms
from django.forms.widgets import DateInput, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *
from school.models import School, Class

from students.models import Student
from teachers.models import Teacher
from subjects.models import Subject
from parents.models import Parent

import re

class CreateUserForm(UserCreationForm):
    USER_TYPE_CHOICES = (("Admin", "Admin"), ("Staff", "Staff"), ("Teacher", "Teacher"), ("Student", "Student"), ("Parent", "Parent"))
    GENDER_CHOICES = [("M", "Male"), ("F", "Female")]

    username = forms.CharField(label='Login', 
                widget=forms.TextInput(attrs={'placeholder': 'Login', 'class': 'form-control'}))

    email = forms.EmailField(label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        error_messages={'invalid': 'Twój email jest nieprawidłowy'})

    first_name = forms.CharField(label='Imię', 
                widget=forms.TextInput(attrs={'placeholder': 'Imię', 'class': 'form-control'}))

    last_name = forms.CharField(label='Nazwisko', 
                widget=forms.TextInput(attrs={'placeholder': 'Nazwisko', 'class': 'form-control'}))

    address = forms.CharField(label='Adres zamieszkania', 
                widget=forms.TextInput(attrs={'placeholder': 'Adres Zamieszkania', 'class': 'form-control'}))

    user_type = forms.ChoiceField(label='Typ użytkownika',
                choices=USER_TYPE_CHOICES,
                widget=forms.Select(attrs={'placeholder': 'Typ użytkownika', 'class': 'form-control'}))

    gender = forms.ChoiceField(label='Płeć',
                choices=GENDER_CHOICES,
                widget=forms.Select(attrs={'placeholder': 'Płeć', 'class': 'form-control'}))

    password1 = forms.CharField(label='Hasło',
        widget=forms.PasswordInput(attrs={'placeholder': 'Hasło', 'class': 'form-control'}))

    password2 = forms.CharField(label='Powtórz hasło',
        widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz Hasło', 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].required = False


    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'address', 'gender', 'user_type', 'password1', 'password2', 'teacher_subject')

    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Ta nazwa użytkownika już istnieje. Wybierz inną.")
        if not len(username) >= 5:
            raise forms.ValidationError("Nazwa użytkownika musi mieć conajmniej 5 znaków.")
        if re.search('\s', username):
            raise forms.ValidationError("Nazwa użytkownika nie może zawierać spacji.")
        if re.search("[!@#$%^&*(),.?\":{}|<>\\/;'[\]-\]]", username):
            raise forms.ValidationError("Nazwa użytkownika nie może zawierać znaków specjalnych oprócz _ (podłogi).")

        return username
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Użytkownik z tym adresem email już istnieje.")
        return email

    def clean_password1(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        if not re.search('[0-9]', password1):
            print("wchodze tutaj")
            raise forms.ValidationError("Twoje hasło musi zawierać przynajmniej jedną cyfrę.")
        if not len(password1) >= 8:
            raise forms.ValidationError("Twoje hasło musi mieć conajmniej 8 znaków.")

        return password1

    def clean_password2(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("Potwierdź swoje hasło.")
        if password1 != password2:
            raise forms.ValidationError("Twoje hasła muszą być takie same.")

        return password2

class CreateStudentForm(forms.Form):

    class_id = forms.ModelChoiceField(
        queryset=Class.objects.all(),
        label='Wybierz klasę',
        empty_label='Wybierz klasę',
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Klasa', 'class': 'form-control'}),
    )

    parent_id = forms.ModelChoiceField(
        queryset=Parent.objects.all(),
        label='Wybierz Opiekuna',
        empty_label='Wybierz opiekuna',
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Opiekun', 'class': 'form-control'}),

    )

class CreateTeacherForm(forms.Form):

    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        label='Wybierz Przedmioty prowadzone przez nauczyciela',
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

# class CreateParentForm(forms.Form):

#     class_id = forms.ModelChoiceField(
#         queryset=Class.objects.all(),
#         label='Wybierz klasę',
#         empty_label='Wybierz klasę',
#         required=False,
#         widget=forms.Select(attrs={'placeholder': 'Klasa', 'class': 'form-control'}),
#     )



# LOGIN

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Login',
                            widget=forms.TextInput(attrs={'placeholder': 'Login', 'class': 'form-control'}),
                            required=False)
    password=forms.CharField(label='Hasło',
                            widget=forms.PasswordInput(attrs={'placeholder': 'Hasło', 'class': 'form-control'}),
                            required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    # def clean(self, *args, **kwargs):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    #     if username and password:
    #         user = authenticate(username=username, password=password)
    #         if not user:
    #             # raise forms.ValidationError("Hasło lub login jest niepoprawne")
    #             pass