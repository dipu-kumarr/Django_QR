from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, QRUserLink

# Customize the User admin panel
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'mobile', 'address')  # Fields to display in the list view
    search_fields = ('name', 'mobile')  # Enable search functionality
    list_filter = ('age',)  # Enable filtering by age

# Customize the QRUserLink admin panel
class QRUserLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'qr_unique_id')  # Fields to display in the list view
    search_fields = ('user__name', 'qr_unique_id')  # Enable search functionality for user name and QR ID
    list_filter = ('user',)  # Enable filtering by user

# Register models with the admin panel
admin.site.register(User, UserAdmin)
admin.site.register(QRUserLink, QRUserLinkAdmin)
