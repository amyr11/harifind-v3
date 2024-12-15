from django.utils.timezone import now
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


class ReturnForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ["returned_to"]

    def __init__(self, *args, **kwargs):
        # Get the item instance passed through the form's initialization
        instance = kwargs.get("instance")
        super().__init__(*args, **kwargs)

        if instance:
            # Filter the 'returned_to' queryset to include only the subscribers of the item
            self.fields["returned_to"].queryset = models.User.objects.filter(
                subscriptions__item=instance
            ).exclude(id=instance.user_id)

    def save(self, commit=True):
        # Only update the specified fields and retain other existing data
        item = super().save(commit=False)
        item.returned = item.returned_to is not None
        item.returned_date = now() if item.returned else None

        if commit:
            # Save the changes to the database
            item.save(update_fields=["returned_to", "returned", "returned_date"])

        return item


class FoundForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ["found_by"]

    def __init__(self, *args, **kwargs):
        # Get the item instance passed through the form's initialization
        instance = kwargs.get("instance")
        super().__init__(*args, **kwargs)

        if instance:
            # Filter the 'found_by' queryset to include only the subscribers of the item
            self.fields["found_by"].queryset = models.User.objects.filter(
                subscriptions__item=instance
            ).exclude(id=instance.user_id)

    def save(self, commit=True):
        # Only update the specified fields and retain other existing data
        item = super().save(commit=False)
        item.returned = item.found_by is not None
        item.returned_date = now() if item.returned else None

        if commit:
            # Save the changes to the database
            item.save(update_fields=["found_by", "returned", "returned_date"])

        return item
