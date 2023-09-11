from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics
from authentication.serializers import RegisterSerializer


class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):                               # post request
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})    # with Serializer, send Request Data(Un/Pwd)
        serializer.is_valid(raise_exception=True)                           # check if request is validated or error
        user = serializer.validated_data['user']                            # getting user password is in background
        token, created = Token.objects.get_or_create(user=user)             # get or create user token
        return Response({                                                   # Response to work with
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username
        })


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
