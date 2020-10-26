from django.urls import path

from authentication.views import registration, sign_in, logoutuser

urlpatterns = [
    path('signUP/', registration, name='Sign Up'),
    path('login/',  sign_in, name='Sign In'),
    path('logout/',  logoutuser, name='sign out')
]