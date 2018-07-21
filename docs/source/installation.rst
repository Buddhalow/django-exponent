Installation
============

1. Install ``django-exponent`` (ideally in your virtualenv!) using pip or simply getting a copy of the code and putting it in a directory in your codebase.

2. Add ``django_exponent`` to your Django settings ``INSTALLED_APPS``:

   .. code-block:: python

       INSTALLED_APPS = [
           # ...
           "django_exponent",
       ]

3. Run ``python manage.py migrate django_exponent``

4. In your projects urls.py, mount the api endpoint for registering push tokens

   .. code-block:: python

       from django_exponents.api import urls as exponent_urls

       ...

       urlpatterns = [
           re_path(r'^exponent/', include(exponent_urls))
       ]


5. Point the code that sends push tokens to http://your-app-path.tld/exponent/token

   .. code-block:: javascript

        import { AsyncStorage } from 'react-native'

        import { Permissions, Notifications } from 'expo';

        export default async function registerForPushNotificationsAsync() {
            let token = await getPushToken()
            let strSession = await AsyncStorage.getItem('@Buddhalow:session')
            let session = null
            if (strSession) {
            session = JSON.parse(strSession)
            } else {
            throw "No session"
            }
            let payload = {
            token: {
                value: token,
            },
            access_token: session.access_token,
            session: session
            }
            let body = JSON.stringify(payload)
            // POST the token to your backend server from where you can retrieve it to send push notifications.
            return await fetch('http://your-app-path.tld/exponent/token', {
            method: 'POST',
            headers: {
                
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: body,
            });
        }

        async function getPushToken() {
            const { status: existingStatus } = await Permissions.getAsync(
                Permissions.NOTIFICATIONS
            );
            let finalStatus = existingStatus;

            // only ask if permissions have not already been determined, because
            // iOS won't necessarily prompt the user a second time.
            if (existingStatus !== 'granted') {
                // Android remote notification permissions are granted during the app
                // install, so this will only ask on iOS
                const { status } = await Permissions.askAsync(Permissions.NOTIFICATIONS);
                finalStatus = status;
            }

            // Stop here if the user did not grant permissions
            if (finalStatus !== 'granted') {
                return;
            }

            // Get the token that uniquely identifies this device
            let token = await Notifications.getExpoPushTokenAsync();
            return token
        }

6. When you want to send a push notification, you create a notification

    .. code-block: python

        from django_exponent.models import PushNotification

        # If you want to send notification to a particular user, do this

        push_notification = PushNotification(
            text='Your text goes here',
            data='',
            user=user
        )

        push_notification.save() # The notification will be sent instantly as you save

         # If you want to send notification to all users of the app, do this

        push_notification = PushNotification(
            text='Your text goes here',
            data=''
        )

        push_notification.save() # The notification will be sent instantly as you save

