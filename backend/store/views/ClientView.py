from rest_framework.decorators import action
from store.views.BaseView import BaseViewSet
from store.serializers import ClientSerializer
from store.repositories.unit_of_work import UnitOfWork
from rest_framework.response import Response

uow = UnitOfWork()

class ClientViewSet(BaseViewSet):
    repo = uow.clients
    serializer_class = ClientSerializer

    @action(detail=False, methods=['get'])
    def by_email(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({'error': 'email parameter required'}, status=400)
        client = uow.clients.find_by_email(email)
        if not client:
            return Response({'error': 'Client not found'}, status=404)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_phone(self, request):
        phone = request.query_params.get('phone')
        if not phone:
            return Response({'error': 'phone parameter required'}, status=400)
        client = uow.clients.find_by_phone(phone)
        if not client:
            return Response({'error': 'Client not found'}, status=404)
        serializer = ClientSerializer(client)
        return Response(serializer.data)