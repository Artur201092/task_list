"""tasklist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from apps.tasks.views import HomeView, delete_task, get_task, add_task, search_tasks

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', HomeView.as_view(template_name="home.html"), name="home"),
    url(r'add-task/$', add_task, name='add_task'),
    url(r'get-task/(?P<pk>\d+)/$', get_task, name='get_task'),
    url(r'delete-task/(?P<pk>\d+)/$', delete_task, name='delete_task'),
    url(r'search-task', search_tasks, name='search_tasks'),
]
