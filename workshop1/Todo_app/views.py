from django.contrib.auth.models import User
from django.shortcuts import render

from Todo_app.models import Todo


def index(req):
    todos = Todo.objects.all()
    context = {
        'todo': todos,
        'users': User.objects.all()
    }

    return render(req, 'todo/index.html', context)
