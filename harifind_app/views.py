from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import logout
from . import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


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


@login_required(login_url="/login")
def edit_profile(request):
    if request.method == "POST":
        form = forms.EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("/settings")
    else:
        form = forms.EditProfileForm(instance=request.user)

    return render(request, "edit-profile.html", {"form": form})


@login_required(login_url="/login")
def change_password(request):
    if request.method == "POST":
        form = forms.ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("/settings")
    else:
        form = forms.ChangePasswordForm(request.user)

    return render(request, "change-password.html", {"form": form})


@login_required(login_url="/login")
def logout_view(request):
    logout(request)
    return redirect("/")


@login_required(login_url="/login")
def settings(request):
    return render(request, "settings.html")


def report(request, type, template):
    if request.method == "POST":
        form = forms.ReportItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.instance.type = type
            form.save()
            return redirect(f"/item/{form.instance.id}")
    else:
        form = forms.ReportItemForm()

    return render(request, template, {"form": form})


@login_required(login_url="/login")
def report_lost(request):
    return report(request, models.Item.Type.LOST, "report-lost.html")


@login_required(login_url="/login")
def report_found(request):
    return report(request, models.Item.Type.FOUND, "report-found.html")


@login_required(login_url="/login")
def view_item(request, item_id):
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


@login_required(login_url="/login")
def add_comment(request, item_id):
    item = get_object_or_404(models.Item, id=item_id)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.instance.item = item
            form.save()

    return redirect(f"/item/{item_id}")


@login_required(login_url="/login")
def edit_item(request, item_id):
    item = get_object_or_404(models.Item, id=item_id, user=request.user)
    form = forms.ReportItemForm(instance=item)

    if request.method == "POST":
        form = forms.ReportItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect(f"/item/{item_id}")

    return render(request, "edit-item.html", {"form": form})


@login_required(login_url="/login")
def delete_item(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(models.Item, id=item_id, user=request.user)
        item.delete()

    return redirect(f"/user/{request.user.username}")


@login_required(login_url="/login")
def view_user(request, username):
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


def listings(request, items, title):
    return render(
        request,
        "listings.html",
        {
            "items": items,
            "title": title,
        },
    )


@login_required(login_url="/login")
def view_lost_items(request):
    return listings(
        request, models.Item.objects.filter(type=models.Item.Type.LOST), "Lost Items"
    )


@login_required(login_url="/login")
def view_found_items(request):
    return listings(
        request, models.Item.objects.filter(type=models.Item.Type.FOUND), "Found Items"
    )


@login_required(login_url="/login")
def view_returned_items(request):
    return listings(
        request, models.Item.objects.filter(returned=True), "Returned Items"
    )
