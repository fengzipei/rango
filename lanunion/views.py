from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.db import transaction
from django.http import HttpResponseRedirect

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth import authenticate, login

from lanunion.forms import UserForm, ProfileForm
from .models import News, Profile


def index(request):
    context = RequestContext(request)

    top_news = News.objects.filter(
        publish_time__lte=timezone.now()
    ).order_by('-publish_time')[:5]

    context_dict = {'top_news': top_news}

    return render(request, 'lanunion/index.html', context_dict, context)


def news_detail(request, news_id):
    context = RequestContext(request)

    news = News.objects.get(id=news_id)

    context_dict = {'news': news}

    return render_to_response('lanunion/news_detail.html', context_dict, context)


def user_login(request):
    context = RequestContext(request)
    context_dict = {}

    # If HTTP POST, pull out form data and process it.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Attempt to log the user in with the supplied credentials.
        # A User object is returned if correct - None if not.
        user = authenticate(username=username, password=password)

        # A valid user logged in?
        if user is not None:
            # Check if the account is active (can be used).
            # If so, log the user in and redirect them to the homepage.
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/lanunion/')
            # The account is inactive; tell by adding variable to the template context.
            else:
                context_dict['disabled_account'] = True
                return render_to_response('lanunion/login.html', context_dict, context)
        # Invalid login details supplied!
        else:
            context_dict['bad_details'] = True
            return render_to_response('lanunion/login.html', context_dict, context)

    # Not a HTTP POST - most likely a HTTP GET. In this case, we render the login form for the user.
    else:
        return render(request, 'lanunion/login.html', context_dict, context)


@login_required
def user_logout(request):
    # As we can assume the user is logged in, we can just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/lanunion/')


@login_required
@transaction.atomic
def profile(request):
    context = RequestContext(request)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    context_dict = {
        'user': User.objects.get(username=request.user),
        'profile': Profile.objects.get(user=request.user),
        'user_form': UserForm(instance=request.user),
        'profile_form': ProfileForm(instance=request.user.profile),
    }

    return render(request, 'lanunion/profile.html', context_dict, context)


def suggest(request):
    pass


def about(request):
    return render(request, 'lanunion/about.html')
