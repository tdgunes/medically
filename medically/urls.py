from django.conf.urls import patterns, include, url
from django.contrib import admin

from web import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Medically.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', views.homepage, name='homepage'),
    url(r'^logout/$', views.logout_view, name="logout_view"),
    url(r'^profile/$', views.profile_view, name="profile_view"),
    url(r'^register/$', views.registration_view, name='new_user'),
    url(r'^activate/(?P<activation_key>\w+)/', views.activation, name='activation'),



    url(r'^new_patient/$', views.new_patient_view, name="new_patient_view"),
    url(r'^(?P<patient_id>\d+)/$', views.patient_view, name='patient'),
    url(r'^(?P<patient_id>\d+)/examination/(?P<examination_id>\d+)/$', views.examination_view, name='examination'),



    url(r'^(?P<patient_id>\d+)/new_examination/$', views.new_examination_view, name='new_examination'),

)
