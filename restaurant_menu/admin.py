from django.contrib import admin
from .models import Item


# Customize how Item model appears in the admin panel
class MenuItemAdmin(admin.ModelAdmin):
    # Columns shown in the list view
    list_display = ("meal", "status")
    # Filter sidebar options
    list_filter = ("status",)
    # Fields to search by
    search_fields = ("meal", "description")


# Register Item model with custom admin configuration
admin.site.register(Item, MenuItemAdmin)
