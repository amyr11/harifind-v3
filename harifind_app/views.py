from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import logout, login
from . import models
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = forms.RegisterForm()

    return render(request, "register/register.html", {"form": form})


def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect("/login")

    if request.method == "POST":
        form = forms.EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("/settings")
    else:
        form = forms.EditProfileForm(instance=request.user)

    return render(request, "edit-profile.html", {"form": form})


def change_password(request):
    if not request.user.is_authenticated:
        return redirect("/login")

    if request.method == "POST":
        form = forms.ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("/settings")
    else:
        form = forms.ChangePasswordForm(request.user)

    return render(request, "change-password.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")


def settings(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    return render(request, "settings.html")


def report(request, type, template):
    if not request.user.is_authenticated:
        return redirect("/login")

    if request.method == "POST":
        form = forms.ReportItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.instance.type = type
            form.save()
            return redirect("/settings")
    else:
        form = forms.ReportItemForm()

    return render(request, template, {"form": form})


def report_lost(request):
    return report(request, models.Item.Type.LOST, "report-lost.html")


def report_found(request):
    return report(request, models.Item.Type.FOUND, "report-found.html")


def view_item(request, item_id):
    if not request.user.is_authenticated:
        return redirect("/login")

    item = get_object_or_404(models.Item, id=item_id)
    comment_form = forms.CommentForm()

    return render(
        request,
        "view-item.html",
        {
            "item": item,
            "comment_form": comment_form,
        },
    )


def add_comment(request, item_id):
    if not request.user.is_authenticated:
        return redirect("/login")

    item = get_object_or_404(models.Item, id=item_id)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.instance.item = item
            form.save()

    return redirect(f"/item/{item_id}")


def edit_item(request, item_id):
    if not request.user.is_authenticated:
        return redirect("/login")

    item = get_object_or_404(models.Item, id=item_id, user=request.user)
    if item:
        form = forms.ReportItemForm(instance=item)
    else:
        return redirect("/settings")

    if request.method == "POST":
        form = forms.ReportItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("/settings")

    return render(request, "edit-item.html", {"form": form})


def delete_item(request, item_id):
    if not request.user.is_authenticated:
        return redirect("/login")

    if request.method == "POST":
        item = get_object_or_404(models.Item, id=item_id, user=request.user)
        if item:
            item.delete()

    return redirect("/settings")


def view_user(request, username):
    if not request.user.is_authenticated:
        return redirect("/login")

    viewing_user = get_object_or_404(models.User, username=username)
    lost_count = viewing_user.reported_items.filter(type=models.Item.Type.LOST).count()
    found_count = viewing_user.reported_items.filter(
        type=models.Item.Type.FOUND
    ).count()
    return render(
        request,
        "view-user.html",
        {
            "viewing_user": viewing_user,
            "lost_count": lost_count,
            "found_count": found_count,
        },
    )


def listings(request, items):
    if not request.user.is_authenticated:
        return redirect("/login")

    return render(request, "listings.html", {"items": items})


def view_lost_items(request):
    return listings(request, models.Item.objects.filter(type=models.Item.Type.LOST))


def view_found_items(request):
    return listings(request, models.Item.objects.filter(type=models.Item.Type.FOUND))


def view_returned_items(request):
    return listings(request, models.Item.objects.filter(returned=True))
