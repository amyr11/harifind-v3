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
    return_form = forms.ReturnForm(instance=item)
    found_form = forms.FoundForm(instance=item)

    return render(
        request,
        "view-item.html",
        {
            "item": item,
            "comment_form": comment_form,
            "return_form": return_form,
            "found_form": found_form,
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
def return_to(request, item_id):
    return return_item(request, item_id, forms.ReturnForm)


@login_required(login_url="/login")
def found_by(request, item_id):
    return return_item(request, item_id, forms.FoundForm)


def return_item(request, item_id, form):
    item = get_object_or_404(models.Item, id=item_id)

    if request.method == "POST":
        form = form(request.POST, instance=item)
        if form.is_valid():
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
    query = request.GET.get("query", "")
    return listings(
        request,
        models.Item.objects.filter(name__contains=query, type=models.Item.Type.LOST, returned=False).order_by(
            "-updated_at"
        ),
        "Lost Items",
    )


@login_required(login_url="/login")
def view_found_items(request):
    query = request.GET.get("query", "")
    return listings(
        request,
        models.Item.objects.filter(
            name__contains=query,
            type=models.Item.Type.FOUND, returned=False
        ).order_by("-updated_at"),
        "Found Items",
    )


@login_required(login_url="/login")
def view_returned_items(request):
    query = request.GET.get("query", "")
    return listings(
        request,
        models.Item.objects.filter(name__contains=query, returned=True).order_by("-returned_date"),
        "Returned Items",
    )


@login_required(login_url="/login")
def view_interactions(request):
    active_subscriptions = request.user.get_subscriptions(active=True)
    inactive_subscriptions = request.user.get_subscriptions(active=False)

    return render(
        request,
        "interactions.html",
        {
            "active_subscriptions": active_subscriptions,
            "inactive_subscriptions": inactive_subscriptions,
            "title": "My Interactions",
        },
    )


@login_required(login_url="/login")
def subscribe(request, item_id):
    if request.method == "POST":
        request.user.subscribe(item_id)

    return redirect(f"/interactions")


@login_required(login_url="/login")
def unsubscribe(request, item_id):
    if request.method == "POST":
        request.user.unsubscribe(item_id)

    return redirect(f"/interactions")
