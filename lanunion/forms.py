from django import forms
from django.contrib.auth.models import User

from lanunion.models import Profile, RepairOrder, Advice, Application, News


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'address', 'phone_number', 'qq_number',)


class ReportForm(forms.ModelForm):
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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('comment',)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content')
