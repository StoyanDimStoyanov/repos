from django.urls import path

from Todo_app.views import index

urlpatterns = [
    path('', index)
]