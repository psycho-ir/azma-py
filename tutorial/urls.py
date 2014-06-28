from tutorial.views import *

__author__ = 'SOROOSH'

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', TutorialView.as_view(), name="home"),
                       url(r'^cat/(?P<category_name>.*)$', TutorialWithCategoryView.as_view(), name="category"),
                       url(r'^(?P<tutorial_name>.*)$', TutorialDetailView.as_view(), name="tutorial")
)

