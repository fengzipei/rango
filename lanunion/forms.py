from django import forms
from django.contrib.auth.models import User

from lanunion.models import Profile, RepairOrder, Advice, Application


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'address')


class RepairForm(forms.ModelForm):
    class Meta:
        model = RepairOrder
        fields = ('problem_text',)


class SuggestForm(forms.ModelForm):
    class Meta:
        model = Advice
        fields = ('content',)


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('reason',)
