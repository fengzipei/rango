from django.conf.urls import url

from . import views

app_name = 'lanunion'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news/(?P<news_id>\w+)/$', views.news_detail, name='news_detail'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^about/$', views.about, name='about'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
]
