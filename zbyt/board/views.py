import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .choices import Choices
from .models import Advert, AdvertFile, user_dir_path
from .forms import AddAdvertForm, RegisterUser, LoginUser, AddAdvertFileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import default_storage


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


@login_required
def add_advert(request):
    if request.method == 'POST':
        has_pictures = False
        upload = None
        print(request.FILES.getlist('file'))
        if request.FILES.getlist('file') is not None:
            has_pictures = True
            upload = request.FILES.getlist('file')
            form = AddAdvertForm(request.POST)
            form2 = AddAdvertFileForm(request.FILES)
        else:
            form = AddAdvertForm(request.POST)
            form2 = form
        if form.is_valid() & form2.is_valid():
            print("POST received")
            advert_creator = User.objects.get(username=request.user.username)
            advert = Advert()
            advert.title = form.cleaned_data['title']
            advert.body = form.cleaned_data['body']
            advert.type = form.cleaned_data['type']
            advert.creator = advert_creator
            advert.pub_date = datetime.datetime.now(datetime.timezone.utc)
            advert.save()
            advert_key = advert.pk
            print("upload")
            print(upload)
            if has_pictures:
                files = AdvertFile(file=upload)
                for file in files.file:
                    print("Dubug files below:")
                    print(file)
                    default_storage.save(user_dir_path(request, file.name), file)
                    Advert.objects.get(pk=advert_key).files.update_or_create(file=file.name)
                    advert.save()
            context = get_top(request)
            return index(request)
        else:
            return HttpResponse("lame")
    else:
        form = AddAdvertForm()
        form_files = AddAdvertFileForm()
        return render(request, 'add.html',
                      {'form': form,
                       "form_files": form_files})


def make_photo_path(request, files):
    urls = []
    for f in files:
        url = '/user_' + request.user.username
        url = f.file.url[0:7] + url + f.file.url[7:]
        urls.append(url)
        print("Debug urls...")
        print(urls)
    return urls


def show_advert(request, advert_id):
    advert = Advert.objects.get(pk=advert_id)
    files = AdvertFile.objects.filter(advert=advert_id)
    urls = make_photo_path(request, files)
    return render(request, 'show.html', {'advert': advert,
                                         'urls': urls})


def login_user(request):
    if request.method == 'POST':
        form = LoginUser(request.POST)
        redirect_to = request.GET.get('next')
        if redirect_to is None:
            redirect_to = '/'
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
            user = User.objects.create_user(form.cleaned_data['username'],
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


def get_top(request):
    latest_advert_list = Advert.objects.order_by('-pub_date')[:10]
    context = {'latest_advert_list': latest_advert_list}
    if request.user.is_authenticated:
        context.update({'logged': True})
    return context


def get_top_types(long=10):
    latest_advert_list_buy = Advert.objects.filter(type=Choices.types[1][0]).order_by('-pub_date')[:long]
    latest_advert_list_sell = Advert.objects.filter(type=Choices.types[0][0]).order_by('-pub_date')[:long]
    latest_advert_list_barter = Advert.objects.filter(type=Choices.types[2][0]).order_by('-pub_date')[:long]
    context = {'latest_advert_buy': latest_advert_list_buy}
    context.update({'latest_advert_sell': latest_advert_list_sell})
    context.update({'latest_advert_barter': latest_advert_list_barter})
    return context


def get_top_categories(long=10):
    latest_advert_list_seed = Advert.objects.filter(category=Choices.categories[1][0]).order_by('-pub_date')[:long]
    latest_advert_list_flower = Advert.objects.filter(category=Choices.categories[0][0]).order_by('-pub_date')[:long]
    latest_advert_list_fiber = Advert.objects.filter(category=Choices.categories[2][0]).order_by('-pub_date')[:long]
    context = {'latest_advert_list_seed': latest_advert_list_seed}
    context.update({'latest_advert_list_flower': latest_advert_list_flower})
    context.update({'latest_advert_list_fiber': latest_advert_list_fiber})
    return context


def category(request, cat):
    context = get_top_categories(40)
    context.update(({'category': cat}))
    return render(request, 'category.html', context)


def by_type(request, typ):
    context = get_top_types(40)
    context.update({'type': typ})
    print(context)
    return render(request, 'type.html', context)


def index(request):
    context = get_top(request)
    types = Choices.types
    context.update({'types': types})
    context.update(get_top_types())
    categories = Choices.categories
    context.update(({'categories': categories}))
    context.update(get_top_categories())
    return render(request, 'index.html', context)
