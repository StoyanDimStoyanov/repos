from django.shortcuts import render

# Create your views here.


def index(req):
    if req.user.is_authenticated:
        context = {
            'msg' : 'True'
        }
    else:
        context = {
            'msg': False
        }

    return render(req, 'landing_page.html', context)