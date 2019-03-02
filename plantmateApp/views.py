from django.shortcuts import render
from django.http import HttpResponse
from plantmateApp.models import Business
from plantmateApp.forms import BusinessForm, UserForm, UserProfileForm


def home(request):
    context_dict = {}
    return render(request, 'plantmate/home.html', context=context_dict)


def businesslist(request):
    context_dict = {}
    return render(request, 'plantmate/business-list.html', context=context_dict)


def show_business(request, business_name_slug):

    context_dict = {}

    try:
        business = Business.objects.get(slug=business_name_slug)
        context_dict['business'] = business

    except Business.DoesNotExist:
        context_dict['business'] = None

    return render(request, 'plantmate/business.html', context_dict)


def add_business(request):
    form = BusinessForm()

    if request.method == 'POST':
        form = BusinessForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print(form.errors)
    return render(request, 'plantmate/add-business.html', {'form': form})


def quiz(request):
    context_dict = {}
    return render(request, 'plantmate/quiz.html', context=context_dict)


def recommendations(request):
    return HttpResponse("recommendations")


def plant(request):
    context_dict = {'boldmessage': "PLANT!"}
    return render(request, 'plantmate/plant.html', context=context_dict)


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
    context_dict = {}
    return render(request, 'plantmate/myaccount.html', context=context_dict)


def plant_list(request):
    context_dict = {'boldmessage': "A LIST OF PLANTS!"}
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






