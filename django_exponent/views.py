import json

from django.http import JsonResponse

from .models import PushToken


def register_token(request):
    """Register push token"""
    try:
        data = json.loads(request.body)
        push_token = PushToken(
            user=User.objects.get(
                username=data.get('user').get('username')
            ),
            token=data.get('token').get('value')
        )
        push_token.save()
        return JsonResponse(
            dict(
                status=201
            )
        )
    except Exception, e:
        return JsonResponse(
            dict(
                status=500,
                error=e.message
            )
        )
