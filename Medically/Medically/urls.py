from django.conf.urls import patterns, include, url
from django.contrib import admin

from MedicallyWeb import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Medically.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^new_patient/$', views.new_patient_view, name="new_patient_view"),
)
