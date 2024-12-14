from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("password_change/", views.change_password, name="password_change"),
    path("logout/", views.logout_view, name="logout"),
    path("", include("django.contrib.auth.urls")),
    path("settings/", views.settings, name="settings"),
    path("report_lost/", views.report_lost, name="report_lost"),
    path("report_found/", views.report_found, name="report_found"),
    path("item/<int:item_id>/", views.view_item, name="view_item"),
    path("item/edit/<int:item_id>/", views.edit_item, name="edit_item"),
    path("item/delete/<int:item_id>/", views.delete_item, name="delete_item"),
    path("item/comment/<int:item_id>/", views.add_comment, name="add_comment"),
    path("user/<str:username>/", views.view_user, name="view_user"),
]
