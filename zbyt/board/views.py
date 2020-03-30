import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Advert, User
from .forms import AddAdvertForm, RegisterUser, LoginUser
from django.contrib.auth.models import User as User2
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


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
    user = User(advert)
    print(user)
    return render(request, 'show.html', {'advert': advert,
                                         'creator': user})


def login_user(request):
    if request.method == 'POST':
        form = LoginUser(request.POST)
        redirect_to = request.GET.get('next')
        if redirect_to is None:
            redirect_to = '/'
        print(form['password'])
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,
                                password=password)
            if user is not None:
                login(request, user)
                return redirect(redirect_to)
            else:
                return HttpResponse("Zły login :>")
        else:
            return HttpResponse("Błąd walidacji")
    else:
        return render(request, 'register.html')


def register(request):
    if request.method == 'POST':
        redirect_to = request.GET.get('next')
        if redirect_to is None:
            redirect_to = '/'
        form = RegisterUser(request.POST)
        print(form['password'])
        if form.is_valid():
            print("POST received")
            user = (form.cleaned_data['username'])
            print(user)
            user = User2.objects.create_user(form.cleaned_data['username'],
                                             form.cleaned_data['email'],
                                             form.cleaned_data['password'])
            user.last_name = form.cleaned_data['last_name']
            user.first_name = form.cleaned_data['first_name']
            user.save()
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            print("user:")
            print(user)
            if user is not None:
                login(request, user)
                print("a little dubugging LOGGED USER @ POST…")
                print(redirect_to)
                return redirect(redirect_to)
            else:
                return HttpResponse("Buba :(")
        else:
            print("Not a valid form!")
            return render(request, 'register.html',
                          {'form': form,
                           'next': redirect_to})
    else:
        redirect_to = request.GET.get('next')
        if request.user.is_authenticated:
            return HttpResponse("elo :)")
        else:
            form = RegisterUser()
            login_form = LoginUser()
            print("a little dubugging @ GET…")
            print(redirect_to)
            return render(request, 'register.html',
                          {'form': form,
                           'next': redirect_to,
                           'login_form': login_form})


def index(request):
    latest_advert_list = Advert.objects.order_by('-pub_date')[:5]
    context = {'latest_advert_list': latest_advert_list}
    if request.user.is_authenticated:
        context.update({'logged': True})
    return render(request, 'index.html', context)
