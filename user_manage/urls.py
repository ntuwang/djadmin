from django.conf.urls import url
from django.contrib.auth import views as djviews
from . import views as uviews
from django.views.generic.base import RedirectView

# app_name = 'user'

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/home/index")),
    url(r'^login/$', uviews.login, name='login'),
    url(r'^logout/$', uviews.logout, {'next_page': '/'}, name='logout'),

]
