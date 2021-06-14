from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from website.models import Ticket, Review


class RegisterForm(UserCreationForm):
    """User registration form."""

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        """Overloads UserCreationForm with fields details."""

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


class AskReviewForm(ModelForm):
    """Ticket creation form."""

    class Meta:
        model = Ticket
        labels = {"title": "Titre", "description": "Description", "image": "Couverture"}
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-textfield"}),
            "description": forms.Textarea(attrs={"class": "form-textfield"}),
        }
        fields = ["title", "description", "image"]


class CreateReviewForm(ModelForm):
    """Review creation form."""

    class Meta:
        model = Review
        labels = {"headline": "Résumé", "rating": "Note", "body": "Contenu"}
        widgets = {
            "headline": forms.TextInput(attrs={"class": "form-textfield"}),
            "body": forms.Textarea(attrs={"class": "form-textfield"}),
        }
        fields = ["headline", "rating", "body"]
