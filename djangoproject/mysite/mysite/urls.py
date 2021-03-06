"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse


def index(request):
    return HttpResponse('This is index page.')


def hello(request):
    return HttpResponse('Hello word!')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^%', index),
    url(r'^hello/$', hello),
    # 如果捕获到带有polls的域名，就交给polls下面的urls处理
    url(r'^polls/', include('polls.urls')),
]
