from django import forms
from django.contrib.auth.models import User
from lanunion.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'address')
