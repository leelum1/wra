from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    # def __init__(self, *args, *kwargs):
    #     super().__init__(*args, *kwargs)
    #     self.fields["username"].label = "Display name"
    #     self.fields["email"].label = "Email address"
