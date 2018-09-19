from django.conf.urls import patterns, url, include
from django.conf.urls.defaults import *
from tastypie import *
from myproject.api.newuser import UsersResource
from myproject.views import first

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()
v1_api = Api(api_name='v1')
v1_api.register(UsersResource())

urlpatterns = patterns('',

	(r'', include(v1_api.urls)),
	url(r'^user/$',first.users123),
)
