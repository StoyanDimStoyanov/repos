from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from common.forms import CommentForm
from common.models import Comment
from pets.forms import PetCreateForm
from pets.models import Pet, Like
from django.contrib import messages


@login_required()
def index(req, *args):
    return render(req, 'pets/pets.html')


@login_required()
def pet_all(req, *args):

    context = {
        'all_pets': reversed(Pet.objects.all().filter(date_created__lt=timezone.now())),
        'messages': args
    }
    return render(req, 'pets/pets.html', context)


@login_required()
def show_pet_detail(req, pk):

    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    comment_form = CommentForm()
    comment = Comment.objects.filter(pet_id=pk)
    context = {
        'pet': pet,
        'comment_form': comment_form,
        'comment': comment,

    }
    return render(req, 'pets/pet_details.html', context)


@login_required()
def like_pet(req, pk):

    pet = Pet.objects.get(pk=pk)
    like = Like()
    like.pet = pet
    like.user_who_liked = req.user.username
    ll = []
    try:
        objects = Like.objects.filter(pet_id=pk)
        for obj in objects:
            if obj.user_who_liked == req.user.username:
                ll.append(True)
            else:
                ll.append(False)
        if any(ll):
            pass
        else:
            like.save()
    except:
        like.save()


    return redirect('pet_detail', pk)


@login_required()
def create(req):
    if req.method == 'GET':
        if Pet.objects.filter(username_id=req.user.id):
            message = 'You already have one animal, you are not allow to create second.'
            return pet_all(req, message)
        context = {
            'create': PetCreateForm(),

        }
        return render(req, 'pets/pet_create.html', context)
    form = PetCreateForm(req.POST)
    if form.is_valid():
        pet = Pet()
        pet.type = form.cleaned_data['type']
        pet.name = form.cleaned_data['name']
        pet.age = form.cleaned_data['age']
        pet.description = form.cleaned_data['description']
        pet.image_url = form.cleaned_data['image_url']
        pet.username_id = req.user.id
        pet.save()
        return redirect('pet_list')


def pet_comment(req, pk):
    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = Comment()
            comment.comment = form.cleaned_data['comment']
            comment.username = req.user.username
            comment.pet_id = pk
            comment.save()
    return show_pet_detail(req, pk)


@login_required()
def your_pet(req):
    if req.method == 'POST':
        return pet_delete(req)
    try:
        pet = Pet.objects.get(username_id=req.user.id)
    except:
        pet = False
    context = {
        'pet': pet,
    }
    return render(req, 'pets/pet_delete.html', context)

@login_required()
def pet_delete(req):
    pet = Pet.objects.get(username_id=req.user.id)
    pet.delete()
    message = 'You have deleted your pet.'
    return pet_all(req, message)