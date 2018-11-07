from django.shortcuts import render
from house.forms import SettingsForm
# Create your views here.
from django.views import View
from house.models import *


def index(request):
    return render(request, template_name="house/index.html" )


def settings(request):
    return render(request, template_name="house/settings.html")

class Settings(View):

    def get(self, request):
        form = SettingsForm()
        return render(request, template_name="house/settings.html", context={'form':form})

    def post(self, request):
        form = SettingsForm(request.POST)
        if form.is_valid():
            HouseSetting.objects.set_new_settings(form.cleaned_data['bedroom_temperature'],
                                             form.cleaned_data['water_temperature'],
                                             form.cleaned_data['light_in_bathroom'],
                                             form.cleaned_data['light_in_bedroom'])
        return render(request, template_name="house/settings.html", context={'form': form})


def user_settings(request):
    return render(request, template_name="house/user_settings.html")


def signup(request):
    return render(request, template_name="house/signup.html")