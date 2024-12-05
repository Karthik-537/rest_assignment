from django.conf.urls import include
from django.urls import re_path

from test_app.build.view_environments.person_create_.router import person_create_


base_path = "api/"

api_paths = [
    re_path(r'^person/create/$', person_create_),
]


urlpatterns = [
    re_path(r'^{base_path}'.format(base_path=base_path), include(api_paths))
]
