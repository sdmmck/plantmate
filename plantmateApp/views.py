from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from plantmateApp.models import Business, Plant, PlantImage, UserWishlistPlants, UserSavedPlants, UserProfile, User
from plantmateApp.forms import BusinessForm, UserForm, UserProfileForm, PlantForm, ImageForm, SavePlantForm, WishlistPlantForm
from django.template.defaultfilters import slugify



def home(request):
    context_dict = {}
    return render(request, 'plantmate/home.html', context=context_dict)


def businesslist(request):
    context_dict = {}

    try:
        business_list = Business.objects.order_by('-name')
        context_dict = {'businesses': business_list}

    except Plant.DoesNotExist:
        context_dict['business'] = None

    return render(request, 'plantmate/business-list.html', context=context_dict)


def show_business(request, business_name_slug):

    context_dict = {}

    try:
        business = Business.objects.get(slug=business_name_slug)
        context_dict['business'] = business

    except Business.DoesNotExist:
        context_dict['business'] = None

    return render(request, 'plantmate/business.html', context_dict)

@login_required
def add_business(request):

    form = BusinessForm()

    if request.method == 'POST':
        form = BusinessForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return show_business(request, slugify(form.__getitem__('name').value()))

        else:
            print(form.errors)
    return render(request, 'plantmate/add-business.html', {'form': form})

@login_required
def save_plant(request):

    save_plant_form = SavePlantForm(request.POST)
    print("no save ----------------------------------------------------------------")

    if save_plant_form.is_valid():
        save_plant_form.save()
        print("hiya ----------------------------------------------------------------")
        return myaccount(request)
    else:
        print(save_plant_form.errors)
        return render(request, 'plantmate/myaccount.html', {'save_plant_form': save_plant_form})


@login_required
def wishlist_plant(request):

    wishlist_plant_form = WishlistPlantForm(request.POST)

    try:
        if wishlist_plant_form.is_valid():
            wishlist = wishlist_plant_form.save(commit=False)
            wishlist.user = request.user
            wishlist.save()
            return myaccount(request)
        else:
            print(wishlist_plant_form.errors)
    except IntegrityError:
        return myaccount(request)

    return render(request, 'plantmate/myaccount.html', {'wishlist_plant_form': wishlist_plant_form})


@login_required
def add_image(request, plant_name_slug):

    context_dict = {}

    plant = Plant.objects.get(slug=plant_name_slug)
    context_dict['plant'] = plant

    if request.method == 'POST':
        form = ImageForm(request.POST)

        if form.is_valid():
            image = form.save(commit=True)
            if 'picture' in request.FILES:
                image.picture = request.FILES['picture']
            context_dict['form'] = form
            image.save()

            return show_plant(request, slugify(form.__getitem__('plant_name').value()))

        else:
            print(form.errors)

    return render(request, 'plantmate/add-image.html', context=context_dict)


def show_plant(request, plant_name_slug):

    context_dict = {}
    image = set()

    try:
        plant = Plant.objects.get(slug=plant_name_slug)

        for i in PlantImage.objects.all():
            image.add(i)

        context_dict['plant'] = plant
        context_dict['image'] = image

    except Plant.DoesNotExist:
        context_dict['plant'] = None
    except PlantImage.DoesNotExist:
        context_dict['image'] = None

    return render(request, 'plantmate/plant.html', context_dict)

@login_required
def add_plant(request):

    form = PlantForm()

    if request.method == 'POST':
        form = PlantForm(request.POST)

        if form.is_valid():
            plant = form.save(commit=True)
            plant.save()
            return show_plant(request, slugify(form.__getitem__('name').value()))

        else:
            print(form.errors)
    return render(request, 'plantmate/add-plant.html', {'form': form})

def quiz(request):
    context_dict = {}
    return render(request, 'plantmate/quiz.html', context=context_dict)


def recommendations(request):
    context_dict = {}
    return render(request, 'plantmate/recommendations.html', context=context_dict)


def login(request):
    context_dict = {}
    return render(request, 'plantmate/login.html', context=context_dict)


def signup(request):
    context_dict = {}
    return render(request, 'plantmate/signup.html', context=context_dict)


def contact(request):
    context_dict = {}
    return render(request, 'plantmate/contact.html', context=context_dict)


def myaccount(request):

    wishlistplants = set()

    for i in UserWishlistPlants.objects.all():
        if i.user == request.user:
            wishlistplants.add(i.wishlist_plant)

    username = User.objects.get(username=request.user)

    context_dict = {'username': username, 'wishlist': wishlistplants}

    return render(request, 'plantmate/myaccount.html', context=context_dict)


def plant_list(request):
    plant_a_z = Plant.objects.order_by('-name')
    context_dict = {'plants': plant_a_z}

    return render(request, 'plantmate/plantlist.html', context=context_dict)


def wishlist(request):
    context_dict = {'boldmessage': "all of the plants I wish I had"}
    return render(request, 'plantmate/wishlist.html', context=context_dict)


def my_plants(request):
    context_dict = {'boldmessage': "all of the plants I already have"}
    return render(request, 'plantmate/myplants.html', context=context_dict)


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'plantmate/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})




