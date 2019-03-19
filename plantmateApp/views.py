from django.contrib.auth.decorators import login_required
from django.core import mail
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from plantmateApp.models import Business, Plant, PlantImage, UserWishlistPlants, UserSavedPlants, UserProfile, User, \
    Comment
from plantmateApp.forms import BusinessForm, ProfileImageForm, PlantForm, ImageForm, SavePlantForm, \
    WishlistPlantForm, CommentForm, ContactForm
from django.template.defaultfilters import slugify
from django.core.mail import send_mail, BadHeaderError


def home(request):
    context_dict = {}
    return render(request, 'plantmate/home.html', context=context_dict)


def businesslist(request):

    business_list = Business.objects.order_by('-name')
    context_dict = {'businesses': business_list}

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
            business = form.save(commit=True)
            return show_business(request, business.slug)

        else:
            print(form.errors)
    return render(request, 'plantmate/add-business.html', {'form': form})


@login_required
def save_plant(request):
    save_plant_form = SavePlantForm(request.POST)
    try:
        if save_plant_form.is_valid():
            saved_plants = save_plant_form.save(commit=False)
            saved_plants.user = request.user
            saved_plants.save()
            return my_plants(request)
        else:
            print(save_plant_form.errors)
    except IntegrityError:
        return myaccount(request)
    return render(request, 'plantmate/myaccount.html', {'save_plant_form': save_plant_form})


@login_required
def wishlist_plant(request):
    wishlist_plant_form = WishlistPlantForm(request.POST)
    try:
        if wishlist_plant_form.is_valid():
            wishlisted = wishlist_plant_form.save(commit=False)
            wishlisted.user = request.user
            wishlisted.save()
            return wishlist(request)
        else:
            print(wishlist_plant_form.errors)
    except IntegrityError:
        return wishlist(request)

    return render(request, 'plantmate/myaccount.html', {'wishlist_plant_form': wishlist_plant_form})


def your_plantmate(request):
    plants = plants_as_list()

    if request.user.is_authenticated():
        wishlistplants = UserWishlistPlants.objects.filter(user=request.user)
        saved_plants = UserSavedPlants.objects.filter(user=request.user)
        context_dict = {'plants': plants, 'wishlistplants': wishlistplants,
                        'saved_plants': saved_plants}

    else:
        context_dict = {'plants': plants}

    return render(request, 'plantmate/your-plantmate.html', context=context_dict)


@login_required
def add_comment(request):
    if request.user.is_authenticated():
        form = CommentForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.plant = Plant.objects.get(slug=comment.plant_slug)
                comment.save()
                return show_plant(request, comment.plant_slug)
            else:
                form = CommentForm()
    context_dict = {'form': form}
    return render(request, 'plantmate/myaccount.html', context=context_dict)


@login_required
def like_comment(request):
    likecom_id = None
    if request.method == 'GET':
        likecom_id = request.GET['comment_id']
    likes = 0
    if likecom_id:
        likecom = Comment.objects.get(id=int(likecom_id))
        if likecom:
            likes = likecom.likes + 1
            likecom.likes = likes
            likecom.save()
    return HttpResponse(likes)


@login_required
def dislike_comment(request):
    discom_id = None
    if request.method == 'GET':
        discom_id = request.GET['comment_id']
    dislikes = 0
    if discom_id:
        dislikecom = Comment.objects.get(id=int(discom_id))
        if dislikecom:
            dislikes = dislikecom.dislikes + 1
            dislikecom.dislikes = dislikes
            dislikecom.save()
    return HttpResponse(dislikes)


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


# have made this login_required to avoid error coming up when user is not logged in


def show_plant(request, plant_name_slug):
    image = set()

    try:
        plant = Plant.objects.get(slug=plant_name_slug)

        for i in PlantImage.objects.all():
            if i.plant_name == plant.slug:
                image.add(i)

        comments = Comment.objects.filter(plant_slug=plant_name_slug)

        if request.user.is_authenticated():
            wishlistplants = UserWishlistPlants.objects.filter(user=request.user)
            saved_plants = UserSavedPlants.objects.filter(user=request.user)
            context_dict = {'plant': plant, 'image': image, 'wishlistplants': wishlistplants,
                            'saved_plants': saved_plants, 'comments': comments}

        else:
            context_dict = {'plant': plant, 'image': image, 'comments': comments}

    except Plant.DoesNotExist:
        context_dict['plant'] = None
    except PlantImage.DoesNotExist:
        context_dict['image'] = None

    return render(request, 'plantmate/plant.html', context_dict)


@login_required
def add_plant(request):
    form = PlantForm(request.POST)

    if request.method == 'POST':
        form = PlantForm(request.POST)

        if form.is_valid():
            plant = form.save(commit=False)
            if 'picture' in request.FILES:
                plant.picture = request.FILES['picture']
            plant.save()
            return show_plant(request, slugify(form.__getitem__('name').value()))

        else:
            print(form.errors)
    return render(request, 'plantmate/add-plant.html', {'form': form})


@login_required
def remove_wishlist_plant(request):
    if request.method == 'POST':
        form = WishlistPlantForm(request.POST)
        if form.is_valid():
            wishlisted_plant = request.POST.get('wishlist_plant')
            plant = UserWishlistPlants.objects.filter(wishlist_plant=wishlisted_plant)
            for p in plant:
                p.delete()
            if 'next' in request.GET:
                return wishlist(request)
            else:
                return show_plant(request, wishlisted_plant)

        else:
            print(form.errors)
    return render(request, 'plantmate/wishlist.html', {'form': form})


@login_required
def remove_saved_plant(request):
    if request.method == 'POST':
        form = SavePlantForm(request.POST)
        if form.is_valid():
            saved_plant = request.POST.get('saved_plant')
            plant = UserSavedPlants.objects.filter(saved_plant=saved_plant)
            for p in plant:
                p.delete()
            if 'next' in request.GET:
                return my_plants(request)
            else:
                return show_plant(request, saved_plant)

        else:
            print(form.errors)
    return render(request, 'plantmate/myplants.html', {'form': form})



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


def quiz(request):
    context_dict = {}
    plants = plants_as_list()
    context_dict['plants'] = plants
    return render(request, 'plantmate/quiz.html', context=context_dict)


def plants_as_list():
    plants = Plant.objects.all().values()
    plants_list = list(plants)
    return JsonResponse(plants_list, safe=False)


def login(request):
    context_dict = {}
    return render(request, 'plantmate/login.html', context=context_dict)


def signup(request):
    context_dict = {}
    return render(request, 'plantmate/signup.html', context=context_dict)


def contact(request):

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email_address = form.cleaned_data['email']
            message = form.cleaned_data['message']
            email = mail.EmailMessage(subject, message, email_address, ['support@plantmate.com'])
            email.send()
            return redirect('successful_email')
    return render(request, 'plantmate/contact.html', {'form': form})


def successful_email(request):
    form = ContactForm()
    context_dict = {'success': "success", 'form': form}
    return render(request, 'plantmate/contact.html', context=context_dict)


def contact_success(request):
    context_dict = {}
    return render(request, 'plantmate/contact-success.html', context=context_dict)


def myaccount(request):
    profile_image_form = ProfileImageForm(data=request.POST)
    saved_plants = set()
    wishlist_plants = set()
    username = User.objects.get(username=request.user)
    user_profile = UserProfile.objects.get_or_create(user=username)[0]
    businesses = Business.objects.order_by('name')

    for wish in UserWishlistPlants.objects.filter(user=request.user):
        wishlist_plants.add(Plant.objects.get(slug=wish.wishlist_plant))

    for saved in UserSavedPlants.objects.filter(user=request.user):
        saved_plants.add(Plant.objects.get(slug=saved.saved_plant))

    context_dict = {'username': username, 'wishlist_plants': wishlist_plants, 'saved_plants': saved_plants,
                    'profile_image_form': profile_image_form, 'user_profile': user_profile, 'businesses': businesses}
    return render(request, 'plantmate/myaccount.html', context=context_dict)


def plant_list(request):
    plant_a_z = Plant.objects.order_by('name')
    context_dict = {'plants': plant_a_z}

    return render(request, 'plantmate/plantlist.html', context=context_dict)


def wishlist(request):
    wishlistplants = UserWishlistPlants.objects.filter(user=request.user)
    plants = set()
    for wish in wishlistplants:
        plants.add(Plant.objects.get(slug=wish.wishlist_plant))

    context_dict = {'wishlist': wishlistplants, 'plants': plants}
    return render(request, 'plantmate/wishlist.html', context=context_dict)


def my_plants(request):
    form = SavePlantForm(request.POST)
    saved_plants = UserSavedPlants.objects.filter(user=request.user)
    plants = set()
    for saved in saved_plants:
        plants.add(Plant.objects.get(slug=saved.saved_plant))

    context_dict = {'saved_plants': saved_plants, 'plants': plants, 'form': form}
    return render(request, 'plantmate/myplants.html', context=context_dict)


def add_profile_image(request):
    context_dict = {}

    user = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileImageForm(request.POST)

        if form.is_valid():
            if 'picture' in request.FILES:
                user.picture = (request.FILES['picture'])
            user.save()
            context_dict['image'] = user.picture
        else:
            print(form.errors)
        return myaccount(request)

    return render(request, 'plantmate/add-profile-image.html', context=context_dict)


def change_password(request):
    return render(request, 'registration/password_change,html')

