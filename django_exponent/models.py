import datetime

from django.db import models
from django.contrib.auth.models import User

from exponent_server_sdk import DeviceNotRegisteredError
from exponent_server_sdk import PushClient
from exponent_server_sdk import PushMessage
from exponent_server_sdk import PushResponseError
from exponent_server_sdk import PushServerError
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError


class PushToken(models.Model):
    token = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    time = models.DateTimeField(default=datetime.datetime.now)


class PushNotification(models.Model):
    """Push Notification"""
    token = models.ForeignKey(PushToken, on_delete=models.CASCADE)
    body = models.TextField()
    data = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        response = PushClient().publish(
            PushMessage(
                to=self.token.token,
                body=self.body
            )
        )
    

        super(PushNotification, self).save(args, kwargs)

    def __str__(self):
        return self.body
