from django import forms

from .models import Comments


class model_form(forms.ModelForm):
    class Meta:
        model = Comments
        fields = "__all__"
        widgets = {
            "name" : forms.TextInput(attrs={
                "placeholder" : "Enter your name",
                "id" : "exampleInputName",
                "class" : "form-control"
            }),
            "email" : forms.EmailInput(attrs={
                "placeholder" : "Enter your email",
                "id" : "exampleInputEmail",
                "class" : "form-control"
            }),
            "message" : forms.TextInput(attrs={
                "placeholder" : "Enter your message",
                "id" : "exampleInputMessage",
                "class" : "form-control"
            })
        }
        labels = {
            "name" : "نام",
            "email" : "ایمیل",
            "message" : "پیام",
        }
        error_messages = {
            "required" : {
                'name' : "You must enter your name",
                'email' : "You must enter your email",
                'message' : "You must enter your message"
            }
        }