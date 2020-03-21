from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from register import views as v

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', views.register, name='register'),
    url(r'^about/$', views.about, name='about'),
    url(r'^index/$', views.index, name='index'),
    url(r'^$', views.homepage, name='homepage'), 
]

urlpatterns += staticfiles_urlpatterns()
