# coding = utf-8

from django.conf.urls import url,include

from . import views

globals()['urlpatterns'] = [
    
    url(r'^upload$', views.UploadView.as_view(impl='upload')),
    url(r'^list$', views.ListView.as_view(impl='list')),
    url(r'^clear$', views.ClearView.as_view(impl='clear')),
    url(r'^mail$', views.MailView.as_view(impl='mail')),

]