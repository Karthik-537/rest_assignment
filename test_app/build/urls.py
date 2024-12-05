from django.urls import re_path

from test_app.build.view_environments.person_create_.router import person_create_


urlpatterns = [
    re_path(r'^person/create/$', person_create_),
]