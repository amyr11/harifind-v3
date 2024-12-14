from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    PasswordChangeForm,
)
from . import models


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    image = forms.ImageField(required=False)
    year_level = forms.IntegerField(required=True)

    class Meta:
        model = models.User
        fields = [
            "image",
            "username",
            "email",
            "first_name",
            "last_name",
            "year_level",
            "password1",
            "password2",
        ]


class EditProfileForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    image = forms.ImageField(required=False)
    year_level = forms.IntegerField(required=True)

    class Meta:
        model = models.User
        fields = [
            "image",
            "username",
            "email",
            "first_name",
            "last_name",
            "year_level",
        ]


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = models.User
        fields = [
            "old_password",
            "new_password1",
            "new_password2",
        ]


class ReportItemForm(forms.ModelForm):
    category = forms.ChoiceField(choices=models.Item.Category.choices)
    date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    location = forms.ChoiceField(choices=models.Item.Location.choices)

    class Meta:
        model = models.Item
        fields = [
            "image",
            "name",
            "category",
            "description",
            "date",
            "location",
        ]


class CommentForm(forms.ModelForm):
    comment = forms.CharField(label="", widget=forms.Textarea(attrs={"rows": 1}))

    class Meta:
        model = models.Comment
        fields = ["comment"]
