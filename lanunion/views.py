from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.utils import timezone

from lanunion.forms import UserForm, ProfileForm, ReportForm, SuggestForm, ApplicationForm, CommentForm, NewsForm
from .models import News, Profile, RepairOrder, Advice, Application


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
                return redirect('/lanunion')
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


@login_required
@transaction.atomic
def report(request):
    context = RequestContext(request)
    context_dict = {
        'report_form': ReportForm(instance=request.user),
    }
    if request.method == 'POST':
        repair_form = ReportForm(data=request.POST)
        if repair_form.is_valid():
            form = repair_form.save(commit=False)
            form.applicant_id = request.user
            form.save()
            return redirect('/lanunion')
        else:
            context_dict['error'] = 'the form is invalid'

    return render(request, 'lanunion/report.html', context_dict, context)


@login_required
@transaction.atomic
def repair(request):
    context = RequestContext(request)
    context_dict = {
        'reports': RepairOrder.objects.filter(status="('waiting for repairing', 'waiting for repairing')"),
    }
    if request.method == 'POST':
        repair_form = ReportForm(data=request.POST)
        if repair_form.is_valid():
            form = repair_form.save(commit=False)
            form.applicant_id = request.user
            form.save()
            return redirect('/lanunion')
        else:
            context_dict['error'] = 'the form is invalid'

    return render(request, 'lanunion/repair.html', context_dict, context)


@login_required
@transaction.atomic
def all_advice(request):
    context = RequestContext(request)
    context_dict = {
        'all_advice': Advice.objects.filter(status="('waiting for repairing', 'waiting for repairing')"),
    }
    if request.method == 'POST':
        repair_form = ReportForm(data=request.POST)
        if repair_form.is_valid():
            form = repair_form.save(commit=False)
            form.applicant_id = request.user
            form.save()
            return render(request, 'lanunion/index.html', context_dict, context)
        else:
            context_dict['error'] = 'the form is invalid'

    return render(request, 'lanunion/repair.html', context_dict, context)


@login_required
def my_orders(request):
    context = RequestContext(request)

    context_dict = {
        'reports': RepairOrder.objects.filter(applicant_id=request.user),
        'repair_orders': RepairOrder.objects.filter(repairer_id=request.user),
    }

    return render(request, 'lanunion/my_orders.html', context_dict, context)


@login_required
@transaction.atomic
def repair_orders(request, report_id):
    context = RequestContext(request)

    if request.method == 'POST':
        if request.POST.get('button') == 'Repair':
            order = RepairOrder.objects.get(order_id=report_id)
            order.status = "('processing', 'processing')"
            order.save()
        elif request.POST.get('button') == 'Finish':
            order = RepairOrder.objects.get(order_id=report_id)
            order.status = "('finished', 'finished')"
            order.repairer_id = request.user
            order.finish_time = timezone.now()
            order.comment = CommentForm(data=request.POST).data['comment']
            order.save()

    context_dict = {
        'repair_order': RepairOrder.objects.get(order_id=report_id),
        'comment_form': CommentForm(instance=request.user)
    }

    return render(request, 'lanunion/order_detail.html', context_dict, context)


@login_required
def all_advice(request):
    context = RequestContext(request)

    if request.user.profile.category == 'super admin':
        context_dict = {
            'all_advice': Advice.objects.count(),
            'unreviewed_advice': Advice.objects.filter(status="('waiting for review', 'waiting for review')"),
            'reviewed_advice': Advice.objects.filter(status="('reviewed', 'reviewed')"),
        }
    else:
        context_dict = {
            'error': "Invalid operation",
        }

    return render(request, 'lanunion/all_advice.html', context_dict, context)


@login_required
def my_applications(request):
    context = RequestContext(request)

    context_dict = {
        'applications': Application.objects.filter(applicant_id=request.user),
    }

    return render(request, 'lanunion/my_applications.html', context_dict, context)


@login_required
def my_advice(request):
    context = RequestContext(request)

    context_dict = {
        'advice': Advice.objects.filter(suggester_id=request.user),
    }

    return render(request, 'lanunion/my_advice.html', context_dict, context)


@login_required
def order_detail(request, order_id):
    context = RequestContext(request)

    repair_order = RepairOrder.objects.get(order_id=order_id)

    if repair_order.applicant_id == request.user or repair_order.repairer_id == request.user:
        context_dict = {
            'repair_order': repair_order,
        }
    else:
        context_dict = {
            'error': "Invalid operation",
        }

    return render(request, 'lanunion/order_detail.html', context_dict, context)


@login_required
def advice_detail(request, advice_id):
    context = RequestContext(request)

    advice = Advice.objects.get(advice_id=advice_id)

    if request.user.profile.category == 'super admin':
        if request.POST.get('button') == 'Submit':
            advice = Advice.objects.get(advice_id=advice_id)
            advice.status = "('reviewed', 'reviewed')"
            advice.reviewer_id = request.user
            advice.review_time = timezone.now()
            advice.comment = CommentForm(data=request.POST).data['comment']
            advice.save()

        context_dict = {
            'advice': advice,
            'comment_form': CommentForm(instance=request.user)
        }

    elif advice.suggester_id == request.user:
        context_dict = {
            'advice': advice,
        }

    else:
        context_dict = {
            'error': "Invalid operation",
        }
    return render(request, 'lanunion/advice_detail.html', context_dict, context)


@login_required
def application_detail(request, application_id):
    context = RequestContext(request)

    application = Application.objects.get(application_id=application_id)

    if application.applicant_id == request.user:
        context_dict = {
            'application': application,
        }
    else:
        context_dict = {
            'error': "Invalid operation",
        }

    return render(request, 'lanunion/application_detail.html', context_dict, context)


@login_required
@transaction.atomic
def suggest(request):
    context = RequestContext(request)
    context_dict = {
        'suggest_form': SuggestForm(instance=request.user),
    }
    if request.method == 'POST':
        suggest_form = SuggestForm(data=request.POST)
        if suggest_form.is_valid():
            form = suggest_form.save(commit=False)
            form.suggester_id = request.user
            form.save()
            return redirect('/lanunion')
        else:
            context_dict['error'] = 'the form is invalid'

    return render(request, 'lanunion/suggest.html', context_dict, context)


@login_required
@transaction.atomic
def apply(request):
    context = RequestContext(request)
    context_dict = {
        'application_form': ApplicationForm(instance=request.user),
    }
    if request.method == 'POST':
        application_form = ApplicationForm(data=request.POST)
        if application_form.is_valid():
            form = application_form.save(commit=False)
            form.applicant_id = request.user
            form.save()
            return redirect('/lanunion')
        else:
            context_dict['error'] = 'the form is invalid'

    return render(request, 'lanunion/apply.html', context_dict, context)


@login_required
@transaction.atomic
def publish_news(request):
    context = RequestContext(request)
    context_dict = {
        'publish_news_form': NewsForm(instance=request.user),
    }
    if request.method == 'POST':
        form = NewsForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.publisher_id = request.user
            form.save()
            return redirect('/lanunion')
        else:
            context_dict['error'] = 'the form is invalid'

    return render(request, 'lanunion/publish_news.html', context_dict, context)


def about(request):
    return render(request, 'lanunion/about.html')
