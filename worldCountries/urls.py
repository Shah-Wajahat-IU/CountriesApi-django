from django.contrib import admin
from django.urls import path
from django.urls.conf import url , include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include('countries.urls')),
]
