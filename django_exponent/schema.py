from django.utils import timezone
from graphene_django import DjangoObjectType
import graphene

from .models import PushNotification


class PushNotificationObjectType(DjangoObjectType):
    class Meta:
        model = PushNotification
