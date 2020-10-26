from django import forms


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class Userform(forms.ModelForm):
#     class Meta:
#         model = Users
#         fields = ['email', 'password', 'password2']
#         password2 = forms.PasswordInput()
#         labels = {
#             'password2': 'Repeat password'
#         }
#         widgets = {
#             'password': forms.PasswordInput(attrs={
#                 'class':'col-12',
#                 'placeholder': "Password"
#             }),
#             'email': forms.EmailInput(attrs={
#                 'class': 'col-12 ',
#                 'placeholder': 'Email',
#
#
#             }),
#             'password2': forms.PasswordInput(attrs={
#                 'class':'col-12 ',
#                 'placeholder': "Repeat password",
#                 'label': 'Repeat password'
#             })
#         }

class CreateUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
                    'password1': forms.PasswordInput(attrs={
                        'class': 'col-12',
                        'placeholder': "Password"
                    }),
                    'email': forms.EmailInput(attrs={
                        'class': 'col-12 ',
                        'placeholder': 'Email',


                    }),
                    'password2': forms.PasswordInput(attrs={
                        'class': 'col-12 ',
                        'placeholder': "Repeat password",
                        'label': 'Repeat password'}),
                    'username': forms.TextInput(attrs={
                        'class': 'col-12',
                        'placeholder': "username"
                    }),
                }
