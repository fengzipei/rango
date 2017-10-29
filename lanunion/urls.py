from django.conf.urls import url

from . import views

app_name = 'lanunion'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news/(?P<news_id>\w+)/$', views.news_detail, name='news_detail'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^about/$', views.about, name='about'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^repair/$', views.repair, name='repair'),
    url(r'^my_orders/$', views.my_orders, name='my_orders'),
    url(r'^my_advice/$', views.my_advice, name='my_advice'),
    url(r'^my_applications/$', views.my_applications, name='my_applications'),
    url(r'^order_detail/(?P<order_id>\w+)/$', views.order_detail, name='order_detail'),
    url(r'^advice_detail/(?P<advice_id>\w+)/$', views.advice_detail, name='order_detail'),
    url(r'^application_detail/(?P<application_id>\w+)/$', views.application_detail, name='application_detail'),
    url(r'^suggest/$', views.suggest, name='suggest'),
    url(r'^apply/$', views.apply, name='Apply'),
]
