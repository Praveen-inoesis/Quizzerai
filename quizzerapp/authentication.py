#quizzerapp\authentication.py

from rest_framework.authentication import BaseAuthentication
from keycloak import KeycloakOpenID
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class KeycloakAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Extract the token from the Authorization header
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header or 'Bearer ' not in auth_header:
            raise AuthenticationFailed('Authorization header missing or invalid.')

        token = auth_header.split('Bearer ')[-1]

        # Keycloak OpenID client
        keycloak_openid = KeycloakOpenID(
            server_url="https://identity.quickans.ai",
            client_id="Quizzer",
            realm_name="Quizzer.ai",
            client_secret_key="oKiZ3JmJ6xjIbLNk75Ortxt4K82C294Y"
            
        )


        try:
            # Verify the token
            user_info = keycloak_openid.userinfo(token)
        except Exception as e:
            print(e)
            raise AuthenticationFailed('Invalid or expired token.')

        # Create or retrieve Django user based on Keycloak user info
        username = user_info.get('preferred_username')
        if not username:
            raise AuthenticationFailed('No username found in token.')

        user, created = User.objects.get_or_create(username=username)

        return user, None


