"""madsoc URL Configuration

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
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='site.html')),
    url(r'^spoergeskema/', TemplateView.as_view(template_name='skema.html'), name='skema'),
    url(r'^deltagelse-i-interview/', TemplateView.as_view(template_name='interview.html'), name='interview'),
    url(r'^om-os/', TemplateView.as_view(template_name='omos.html'), name='omos'),
    url(r'^kontakt/', TemplateView.as_view(template_name='kontakt.html'), name='kontakt'),
    #url(r'^blog/$', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
