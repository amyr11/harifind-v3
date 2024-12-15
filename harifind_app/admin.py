from django.contrib import admin
from . import models


# Inline admin for Comments
class CommentInline(
    admin.TabularInline
):  # or use admin.StackedInline for a detailed layout
    model = models.Comment
    extra = 0  # Number of empty forms to display


class SubscriptionInline(admin.TabularInline):
    model = models.Subscription
    extra = 0


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "year_level",
        "degree",
        "date_joined",
        "last_login",
    )
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_active", "date_joined", "last_login")
    ordering = ("date_joined",)


# Register your models here
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "returned",
        "returned_to",
        "category",
        "location",
        "type",
        "date",
        "user",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "category", "location", "type", "date")
    list_filter = ("returned", "category", "location", "type", "date")
    ordering = ("created_at",)
    inlines = [CommentInline, SubscriptionInline]  # Attach the inline to ItemAdmin


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "item",
        "user",
        "comment",  # Corrected to match the model field name
        "created_at",
        "updated_at",
    )
    search_fields = (
        "item__name",
        "user__username",
        "comment",
    )  # Improved search fields
    list_filter = ("created_at", "updated_at")
    ordering = ("created_at",)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "item", "active", "subscribed_at", "updated_at")
    search_fields = ("user__username", "item__name")
    list_filter = ("user", "item")
    ordering = ("user", "item")


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Subscription, SubscriptionAdmin)
