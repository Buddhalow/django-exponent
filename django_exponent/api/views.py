import json

from django.http import JsonResponse
from django.contrib.auth.models import User
from oauth2_provider.models import AccessToken

from ..models import PushToken

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register_token(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        token = data.get('token').get('value')
        access_token=data.get('access_token')
        session = data.get('session', None)
        access_token = AccessToken.objects.get(token=access_token)

        user = access_token.user

        push_token, created = PushToken.objects.get_or_create(
            user=user,
            active=True,
            token=token
        )
        push_token.save()

        if session:
            acess_token = AccessToken.objects.get(
                token=session.get('access_token')
            )
            user = access_token.user
        
            push_token.user = user
            push_token.save()

        return JsonResponse(
            dict(
                active=True
            )
        )
    else:
        return JsonResponse(
            dict(
                error='Only POST is supported',
                status=403
            )
        )


def push_notification(request):
    if request.method == 'POST':
        data = json.loads(request.json)
        username = data.get('user').get('username')
        user = request.user
        token = Token.objects.get(user=user)
        message = data.get(
            message=message
        )
        push_notification = PushNotification(
            token=token,
            body=message,
            data=''
        )
        push_notification.save()
    else:
        return JsonResponse(
            dict(
                error='Only POST is supported',
                status=403
            )
        )