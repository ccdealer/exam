from datetime import timedelta

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from django.utils import timezone

from clients.models import Client
from clients.serializers import ClientModelSerializer


class ClientRegistrationModelVIewSet(
    mixins.CreateModelMixin,
    GenericViewSet):

    permission_classes = [AllowAny]
    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer

    @swagger_auto_schema(request_body=ClientModelSerializer)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    

class ClientActivation(
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    permission_classes = [AllowAny]
    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer

    def retrieve(self, request:Request, pk:int):
        activation_code = request.query_params.get("code")
        now = timezone.now()
        try:
            client:Client = Client.objects.get(pk=pk, activation_code = activation_code)
        except Client.DoesNotExist:
            raise Response(data="user not found")
        experetion = client.code_experetion_date

        if experetion <= now:
            return Response(data="Время вышло")
        client.is_active = True
        client.save() 
        return Response(data={"message": "user activated "})

class ClientModelViewSet(ModelViewSet):

    permission_classes = [AllowAny]
    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer

    @swagger_auto_schema()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema()
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

