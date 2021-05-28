from django.urls import path
# This gives an access to TOKEN if we send a username and password
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', obtain_auth_token, name = 'login'),
]