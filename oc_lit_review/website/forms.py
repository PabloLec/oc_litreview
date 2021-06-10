from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = forms.TextInput(
            attrs={
                "placeholder": "Nom d'utilisateur",
                "id": "username",
                "class": "form-control",
            }
        )
        self.fields["password1"].widget = forms.TextInput(
            attrs={
                "placeholder": "Mot de passe",
                "id": "password1",
                "class": "form-control",
                "type": "password",
            }
        )
        self.fields["password2"].widget = forms.TextInput(
            attrs={
                "placeholder": "Confirmez le mot de passe",
                "class": "form-control",
                "type": "password",
            }
        )

    def clean(self):
        cd = self.cleaned_data
        if cd.get("password1") != cd.get("password2"):
            self.add_error("password2", "passwords do not match !")
        return cd
