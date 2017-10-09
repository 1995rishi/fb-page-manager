from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='Login'),
    url(r'^pages', views.pages, name='Page List'),
    url(r'^getPageDetails', views.getPageDetails, name='Page Details'),
    url(r'^updatePageDetails', views.updatePageDetails, name='Update Details'),
]