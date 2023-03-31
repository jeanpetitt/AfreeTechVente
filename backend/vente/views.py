from rest_framework import status, viewsets, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import login, logout
from .models import *
from .serialiser import *


# vues permettant d'acceder au fruit
class FruitViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
	permission_classes = (permissions.AllowAny,)
	serializer_class = FruitSerialiser
	queryset = Fruit.objects.all()
    

# poster un fruit destiner pour la vente
class FruitViewsetPost(viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes= (SessionAuthentication)
    serializer_class = FruitSerialiser
    queryset = Fruit.objects.all()

# modifier un fruit ceci concerne plus son etat
class FruitViewsetUpdate(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes= (SessionAuthentication)
    serializer_class = FruitSerialiser
    queryset = Fruit.objects.all()

# vues d'inscription d'un utilisateur
class UserRegisterViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerialiser
    queryset = Utilisateur.objects.all()


# vues permettant de mettre ajour un utilisateur
class UserViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (SessionAuthentication)
    serializer_class = UserSerialiser
    queryset = Utilisateur.objects.all()




"""
    create view to login user
"""
class UserLoginView(APIView):
    permission_classes = (permissions.AllowAny, )
    authentication_classes = (SessionAuthentication,)

    # metho post to check user authenticate
    def post(self, request):
        data = request.data
        
        serializer = UserLoginSerialiser(data=data)

        if serializer.is_valid(raise_exception=True):
            
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
    



"""
    create view to logout user
"""
class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
