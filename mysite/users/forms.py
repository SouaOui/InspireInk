from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': 'Choose a unique username',
            'email': 'Enter a valid email address.',
            'password1': 'password with at least 8 characters.',
            'password2': 'Re-enter your password to confirm.',
        }

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'password with at least 8 characters.'
        self.fields['password2'].help_text = 'Re-enter your password to confirm.'


class UserUpdateForm(forms.ModelForm):
        email = forms.EmailField()

        class Meta:
            model = User
            fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
     class Meta:
          model = Profile
          fields = ['image']