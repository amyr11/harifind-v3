from django.contrib import admin
from . import models


# Inline admin for Comments
class CommentInline(
    admin.TabularInline
):  # or use admin.StackedInline for a detailed layout
    model = models.Comment
    extra = 0  # Number of empty forms to display


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
    inlines = [CommentInline]  # Attach the inline to ItemAdmin


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


admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Comment, CommentAdmin)
