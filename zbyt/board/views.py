import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Advert, User
from .forms import AddAdvertForm, RegisterUser
from django.contrib.auth.models import User as User2
from django.contrib.auth.decorators import login_required


@login_required
def add_advert(request):
    if request.method == 'POST':
        form = AddAdvertForm(request.POST)
        if form.is_valid():
            print("POST received")
            print(form.cleaned_data)
            advert_creator = User
            advert_creator.first_name = form.cleaned_data['first_name']
            advert_creator.last_name = form.cleaned_data['title']
            advert = Advert()
            advert.title = form.cleaned_data['title']
            advert.body = form.cleaned_data['body']
            advert.type = form.cleaned_data['type']
            advert.creator = advert_creator
            advert.pub_date = datetime.datetime.now(datetime.timezone.utc)
            advert.save()
            return HttpResponse("Thanks!")
    else:
        form = AddAdvertForm()
        return render(request, 'add.html',
                      {'form': form})


def show_advert(request, advert_id):
    advert = get_object_or_404(Advert, pk=advert_id)
    user = User()
    creator = User.objects.get(pk=1)
    return render(request, 'show.html', {'advert': advert,
                                         'creator': creator})


def register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            print("POST received")
            print(form.cleaned_data)
            user = User2.objects.create_user(form.cleaned_data['username'],
                                             form.cleaned_data['email'],
                                             form.cleaned_data['password'])
            user.last_name = form.cleaned_data['last_name']
            user.first_name = form.cleaned_data['first_name']
            user.save()
            return redirect(index)
    else:
        form = RegisterUser()
        return render(request, 'register.html',
                      {'form': form})


def index(request):
    latest_advert_list = Advert.objects.order_by('-pub_date')[:5]
    context = {'latest_advert_list': latest_advert_list}
    return render(request, 'index.html', context)
