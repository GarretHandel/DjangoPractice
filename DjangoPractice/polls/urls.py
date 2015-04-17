from django.conf.urls import url, patterns

from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^admin/', include(admin.site.urls)),
)