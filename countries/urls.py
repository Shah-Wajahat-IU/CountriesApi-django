from django.conf.urls import url
from django.urls.resolvers import URLPattern
from countries import views

urlpattern=[
    url(r'^api/countries$',views.countries_list),
    url(r'^api/countries/(?P<pk>[0-9]+)$',views.countries_detail)
]