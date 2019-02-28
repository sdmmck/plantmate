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


def show_business(request):
    # Create a context dictionary which we can pass
    # to the template rendering engine.

    context_dict = {}

    # try:
    #     business = Business.objects.get(slug=business_name_slug)
    #     context_dict['business'] = business
    #
    # except Business.DoesNotExist:
    #     context_dict['business'] = None

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
# A boolean value for telling the template
# whether the registration was successful.
# Set to False initially. Code changes value to
# True when registration succeeds.
    registered = False
# If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
# Attempt to grab information from the raw form information.
# Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
# If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
# Save the user's form data to the database.
            user = user_form.save()
# Now we hash the password with the set_password method.
# Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
# Now sort out the UserProfile instance.
# Since we need to set the user attribute ourselves,
# we set commit=False. This delays saving the model
# until we're ready to avoid integrity problems.

            profile = profile_form.save(commit=False)
            profile.user = user
# Did the user provide a profile picture?
# If so, we need to get it from the input form and
#put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
# Now we save the UserProfile model instance.
            profile.save()
# Update our variable to indicate that the template
# registration was successful.
            registered = True
        else:
# Invalid form or forms - mistakes or something else?
# Print problems to the terminal.
            print(user_form.errors, profile_form.errors)
    else:
# Not a HTTP POST, so we render our form using two ModelForm instances.
# These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()
# Render the template depending on the context.
    return render(request,
                'plantmate/register.html',
                {'user_form': user_form,
                'profile_form': profile_form,
                'registered': registered})





