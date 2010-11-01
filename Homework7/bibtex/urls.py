from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
name = "This time"

urlpatterns = patterns('articles.views',
    # home page
	url(r'^$', 'collections', kwargs={"template_name": "home.html"}),
	
	# inserting collections
    url(r'^insert_collection.html/$', 'upload_file', kwargs={"template_name": "insert.html"}),
	
	# Query Articles
	url(r'^query.html/$', 'db_query', kwargs={"template_name": "query.html"}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
