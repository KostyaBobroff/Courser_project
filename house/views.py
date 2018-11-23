from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from house.forms import SettingsForm, SignUpForm, SignInForm, UserSettingsForm
# Create your views here.
from django.views import View
from house.models import *
import requests
from django.core.cache import cache



@login_required
def index(request):
    # cache.set('id', request.user.id )
    user_id_list = cache.get('ids')
    if not user_id_list:
        user_id_list = []
    if request.user.id not in user_id_list:
        user_id_list.append(request.user.id)
    cache.set('ids', user_id_list)

    # cache.lpush("user_ids", request.user.id)

    # response =  requests.get("http://smarthome.t3st.ru/api/user.controller",
    #                             headers={'Authorization':
    #                                          'Bearer {}'.format(request.user.api_key)})
    #
    # data = {elem['name']:elem['value'] for elem in response.json()['data']}
    #
    data = cache.get("data_{}".format(request.user.id))
    return render(request, template_name="house/index.html", context={'data': data})


class Settings(LoginRequiredMixin, View):

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



class SignUpView(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, template_name="house/signup.html", context={'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user =  form.save()
            login(request, user)
            return redirect("index")
        return render(request, template_name="house/signin.html", context={'form': form})


class SignInView(View):

    def get(self, request):
        form = SignInForm()
        return render(request, template_name='house/signin.html', context={'form':form, 'next':request.GET.get('next')})

    def post(self, request):
        form = SignInForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(request.POST.get('next'))
        return render(request, template_name='house/signin.html', context={'form':form, 'next':request.POST.get('next')})


class UserSettingView(LoginRequiredMixin, View):

    def get(self, request):
        form = UserSettingsForm()
        return render(request, template_name='house/user_settings.html', context={'form': form})

    def post(self, request):
        form = UserSettingsForm(request.POST)
        if form.is_valid():
            user = form.update(request.user)
            login(request, user)
            return redirect('index')
        return render(request, template_name='house/user_settings.html', context={'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('signin')