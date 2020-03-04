"""djadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('home/', include('home.urls')),
    path('form/', include('form.urls')),
    path('ui/', include('ui.urls')),
    path('table/', include('table.urls')),
    path('chart/', include('chart.urls')),
    path('page/', include('page.urls')),
    path(r'', include('user_manage.urls')),
]
