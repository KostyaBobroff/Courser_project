from django import forms
from django.contrib.auth import login

from house.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SettingsForm(forms.Form):
    bedroom_temperature = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'validate',
                                                                             'min':'16',
                                                                             'max':'50',
                                                                             'value':'21'}))
    water_temperature = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'validate',
                                                                             'min': '24',
                                                                             'max': '90',
                                                                             'value': '80'}))

    light_in_bathroom = forms.BooleanField(widget=forms.CheckboxInput(),initial=False)
    light_in_bedroom = forms.BooleanField(widget=forms.CheckboxInput(), initial=False)



class UserSettingsForm(forms.ModelForm):
    # new_first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'validate'}))
    # new_email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'validate'}))
    # new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'validate'}))
    # new_api_key = forms.CharField(widget=forms.TextInput(attrs={'class':'validate'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'api_key']
        widgets = {
            'username': forms.TextInput(attrs={'class':'validate'}),
            'email': forms.EmailInput(attrs={'class':'validate'}),
            'password': forms.PasswordInput(attrs={'class':'validate'}),
            'api_key': forms.TextInput(attrs={'class':'validate'})
        }

    def update(self, user):
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.set_password(self.cleaned_data.get('password'))
        user.api_key = self.cleaned_data.get('api_key')
        user.save()
        return user
    # def save(self, commit=True):
    #     user = super(UserSettingsForm, self).save(commit=False)
    #     user.username = self.cleaned_data.get('username')
    #     user.email = self.cleaned_data.get('email')
    #     user.set_password(self.cleaned_data.get('password'))
    #     user.api_key = self.cleaned_data.get('api_key')
    #     if commit:
    #         user.save()
    #     return user

class SignUpForm(UserCreationForm):
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={'class':'validate'}))
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'validate'}))
    api_key = forms.CharField(widget=forms.TextInput(attrs={'class':'validate'}))

    class Meta:
        model = User
        fields = ['username', ]
        widgets = {
            'username': forms.TextInput(attrs={'class':'validate'}),
        }

    def clean_username(self):
        data = self.cleaned_data.get('username')
        try:
            u = User.objects.get(username=data)
            raise forms.ValidationError('this user already exist')
        except User.DoesNotExist:
            return data


    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.api_key = self.cleaned_data.get('api_key')

        if commit:
            user.save()
        return user


class SignInForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'validate'}))




