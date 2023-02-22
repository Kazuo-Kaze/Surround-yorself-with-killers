from django import forms
from .models import UserEmail, MailMessage
from django.forms import EmailInput, TextInput, Textarea

class EmailForm(forms.ModelForm):
    class Meta:
        model = UserEmail
        fields = ['email', ]
        widgets = {
            'email': EmailInput(attrs={
                'class': "home__input1", 
                'placeholder': 'Enter your Email',
                'required': 'False'
                })
        }
        labels = {
            "email": "",
        }


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = ['title', 'first_para', 'second_para', 'third_para', 'fourth_para', 'fifth_para', 'image', ]

        widgets = {
            'email': TextInput(attrs={
                'class': "home__text1", 
                'placeholder': 'Enter your Title',
                'required': 'False'
                })
        }

        


