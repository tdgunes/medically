from django.conf.urls import patterns, include, url
from django.contrib import admin

from web import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Doctor component related URLs
    url(r'^$', views.homepage, name='homepage'),
    url(r'^logout/$', views.logout_view, name="logout_view"),
    url(r'^profile/$', views.profile_view, name="profile_view"),
    url(r'^register/$', views.registration_view, name='new_user'),
    url(r'^activate/(?P<activation_key>\w+)/', views.activation, name='activation'),

    # Patient component related URLs
    url(r'^new_patient/$', views.new_patient_view, name="new_patient_view"),
    url(r'^(?P<patient_id>\d+)/$', views.patient_view, name='patient'),
    url(r'^(?P<patient_id>\d+)/examination/(?P<examination_id>\d+)/$', views.examination_view, name='examination'),
    url(r'^search/$', views.search_view, name="search_view"),

    # Examination component related URLs
    url(r'^(?P<patient_id>\d+)/new_examination/$', views.new_examination_view, name='new_examination'),
    
    # Surgery component related URLs
    url(r'^(?P<patient_id>\d+)/examination/(?P<examination_id>\d+)/new_surgery/$',
                           views.new_surgery_view, name='new_surgery'),
    url(r'^(?P<patient_id>\d+)/examination/(?P<examination_id>\d+)/surgery/(?P<surgery_id>\d+)/$',
        views.surgery_view, name='surgery'),

    # Followup component related URLs
    url(r'^(?P<patient_id>\d+)/examination/(?P<examination_id>\d+)/new_followup/$',
        views.new_followup_view, name='new_followup'),
    url(r'^(?P<patient_id>\d+)/examination/(?P<examination_id>\d+)/followup/(?P<followup_id>\d+)/$',
        views.followup_view, name='followup'),

)
