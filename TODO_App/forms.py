from django.forms import *
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email"]
        widgets = {
            "username": TextInput(attrs={
                'class': "form control",
                'placeholder': 'Введите имя'
            }),
            "password": TextInput(attrs={
                'class': 'form control',
                'placeholder': 'Введите пароль'
            }),
            "email": EmailInput(attrs={
                'class': 'form control',
                'placeholder': 'Введите почту'
            })
        }
