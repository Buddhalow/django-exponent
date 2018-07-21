from django.contrib import admin

from django_exponent.models import PushNotification, PushToken


class PushNotificationInline(admin.TabularInline):
    model = PushNotification


@admin.register(PushToken)
class PushToken(admin.ModelAdmin):
    inlines = [PushNotificationInline,]


@admin.register(PushNotification)
class PushNotificationAdmin(admin.ModelAdmin):
    pass
