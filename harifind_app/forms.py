from django.utils.timezone import now
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    PasswordChangeForm,
)
from . import models
from crispy_forms.layout import Layout, Field, Div, Submit, HTML
from crispy_forms.helper import FormHelper

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    image = forms.ImageField(required=False)
    year_level = forms.IntegerField(required=True)
    degree = forms.ChoiceField(choices=models.User.Degree.choices, required=True)

    class Meta:
        model = models.User
        fields = [
            "image",
            "username",
            "email",
            "first_name",
            "last_name",
            "year_level",
            "degree",
            "password1",
            "password2",
        ]

class EditProfileForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    image = forms.ImageField(widget=forms.FileInput, required=False)
    year_level = forms.IntegerField(required=True)
    degree = forms.ChoiceField(choices=models.User.Degree.choices, required=True)
    
    class Meta:
        model = models.User
        fields = [
            "image",
            "username",
            "email",
            "first_name",
            "last_name",
            "year_level",
            "degree",
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-profile-form'
        self.helper.form_class = "border p-8"

        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        HTML("""<img id="image-preview" src="{% if form.image.value %}{{ form.image.value.url }}{% endif %}" class=" mb-4">"""),
                        css_class="w-24 h-24 rounded-full",
                    ),
                    css_class="avatar justify-center mb-4",
                ),
                Field('image', css_class='form-control bg-gray-600 border border-gray-600 rounded-l font-semibold cursor-pointer text-sm', onchange="previewImage(event)"),
                css_class="flex grid grid-cols-2 gap-8 items-center",
            ),
            'username',
            Div(
                Div(
                    Field('first_name', css_class='form-control'),
                    css_class='w-full '),
                Div('last_name', css_class='w-full '),
                css_class='flex grid grid-cols-2 gap-4 mt-4',
            ),
            Div(
                Div('email', css_class='form-control w-full'),
                Div('year_level', css_class='form-control w-full'),
                css_class='flex grid grid-cols-2 gap-4 mt-4 w-full',
            ),
                Field('degree', css_class='form-control'),
            Div(
                HTML('<a class="btn btn-warning form-group" href="javascript:history.back()">Cancel</a>'),
                Submit('submit', 'Save', css_class='btn flex flex-row bg-[#62B096] text-white'),
                css_class='flex grid grid-cols-2 gap-4 justify-end mt-4',
            ),
        )


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = models.User
        fields = [
            "old_password",
            "new_password1",
            "new_password2",
        ]

    def __init__ (self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-password-form'
        self.helper.form_class = "border p-8"
        self.helper.layout = Layout(
            'old_password',
            'new_password1',
            'new_password2',
            Div(
                HTML('<a class="btn btn-warning form-group" href="javascript:history.back()">Cancel</a>'),
                Submit('submit', 'Save', css_class='btn flex flex-row bg-[#62B096] text-white'),
                css_class='flex grid grid-cols-2 gap-4 justify-end mt-4',
            ),
        )


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
    comment = forms.CharField(
        label="", widget=forms.TextInput(attrs={"placeholder": "Add comment..."})
    )

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
