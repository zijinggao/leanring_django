from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from . import views
LoginView.template_name='users/login.html'
urlpatterns =[
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$',views.register, name='register'),
]
