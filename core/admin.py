from django.contrib import admin

from core.models import UserProfile, UserFinancialSettings


class UserFinancialSettingsInline(admin.StackedInline):
    model = UserFinancialSettings


class UserProfileAdmin(admin.ModelAdmin):
    inlines = [
        UserFinancialSettingsInline,
    ]

admin.site.register(UserProfile, UserProfileAdmin)
