from django import forms


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



class UserSettingsForm(forms.Form):
    new_first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'validate'}))
    new_email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'validate'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'validate'}))
    new_api_key = forms.CharField(widget=forms.TextInput(attrs={'class':'validate'}))

    
