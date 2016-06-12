from django.contrib.auth import get_user_model
from django.forms import ModelForm, HiddenInput
from .models import UserFinancialSettings

class UserEditForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'address', 'address_2', 'city', 'state', 'country']


class UserFinancialSettingsForm(ModelForm):
    class Meta:
        model = UserFinancialSettings
        fields = ['publisher_owner', 'payment_method', 'payment_email', 'payment_terms', 'payment_minimum']
