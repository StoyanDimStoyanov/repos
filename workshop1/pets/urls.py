from django.urls import path

from pets.views import pet_all, show_pet_detail, like_pet, create, pet_comment, your_pet

urlpatterns = [
    path('', pet_all, name='pet_list'),
    path('details/<int:pk>', show_pet_detail, name='pet_detail'),
    path('like/<int:pk>', like_pet, name='like pet'),
    path('create/', create, name='pet create'),
    path('comment/<int:pk>', pet_comment, name='pet comment'),
    path('delete/', your_pet, name='delete pet')
]
