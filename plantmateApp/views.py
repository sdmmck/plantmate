from django.shortcuts import render
from django.http import HttpResponse
from plantmateApp.models import Business
from plantmateApp.forms import BusinessForm


def home(request):
    context_dict = {}
    return render(request, 'plantmateApp/home.html', context=context_dict)


def businesslist(request):
    context_dict = {}
    return render(request, 'plantmateApp/business-list.html', context=context_dict)


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

    return render(request, 'plantmateApp/business.html', context_dict)


def add_business(request):
    form = BusinessForm()

    if request.method == 'POST':
        form = BusinessForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print(form.errors)
    return render(request, 'plantmateApp/add-business', {'form': form})




