from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get("username")
        if username is None:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed("Please provide valid credential to access endpoint")
        return user, None


class CustomKeyBasedAuth(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get("username")
        key = request.GET.get("key")
        if username is None:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed("Please provide valid credential to access endpoint")
        c1 = len(key) == 7
        c2 = key[0] == username[-1].lower()
        c3 = key[2] == 'Z'
        c4 = key[4] == username[2].upper()
        c5 = key[6] == '0'
        if c1 and c2 and c3 and c4 and c5:
            return user, None
        raise AuthenticationFailed("Please provide valid key to access endpoint")

# Rules for secrete key:
# 1. key should be of 7 char
# 2. 1st char should be username's last lower char
# 3. 3rd char should be 'Z'
# 4. 5th char should be username's 3rd upper char
# 5. 7th char should be username's 1st char
# http://127.0.0.1:8000/api/?username=shetty&key=yAZbEu0
