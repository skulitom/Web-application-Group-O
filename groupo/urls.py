"""groupo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.views.generic import CreateView
from django.conf.urls import url
from django.contrib import admin
from groupo import views
from django.contrib.auth import views as auth_views
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

urlpatterns = [
  url(r'^$', views.CitationsList.as_view(), name='citation_list'),
  url(r'^citations/$', views.CitationsList.as_view(), name='citation_list'),
  url(r'^new/$', views.CitationCreate.as_view(), name='citation_new'),
  url(r'^edit/(?P<pk>\d+)$', views.CitationUpdate.as_view(), name='citation_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.CitationDelete.as_view(), name='citation_delete'),
  url(r'^login/$',
    login, {'template_name': 'groupo/login.html'}
),
  url(r'^logout/$',
    logout, {'next_page': '/login/'}
),
  url('^register/', CreateView.as_view(
            template_name='groupo/register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    url(r'^admin/', admin.site.urls),
]
