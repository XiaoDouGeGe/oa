# coding = utf-8

from django.conf.urls import url,include

from . import views

globals()['urlpatterns'] = [
    
    url(r'^login$', views.LoginView.as_view(impl='login')),
    url(r'^logout$', views.LogoutView.as_view(impl='logout')),

]