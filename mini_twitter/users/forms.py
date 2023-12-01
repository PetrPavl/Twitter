# from django import forms
# from .models import User
#
#
# class UserForm(forms.ModelForm):
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'profile_picture']
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailField(unique=True),
#             'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
#         }