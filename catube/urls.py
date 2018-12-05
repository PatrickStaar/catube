"""catube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
                  url(r'^$', views.index),
                  url(r'^index$', views.index),
                  url(r'^home$', views.homepage),
                  url(r'^category$', views.category_view),
                  url(r'^login$', views.perform_login),
                  url(r'^signup$', views.signup),
                  url(r'^signin$', views.perform_register),
                  url(r'^upload$', views.load_upload),
                  url(r'^check_upload$', views.perform_upload),
                  url(r'^my_sharing$', views.my_sharing),
                  url(r'^delete$', views.perform_delete),
                  url(r'^profile$', views.profile),
                  url(r'^withdraw$', views.withdraw),
                  url(r'^settings$', views.settings),
                  url(r'^search$', views.search),
                  url(r'^change_pass$', views.perform_password),
                  url(r'^clean_content$', views.perform_clean_content),
                  url(r'^clean_account$', views.perform_clean_account),
                  url(r'^admin/', admin.site.urls)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)