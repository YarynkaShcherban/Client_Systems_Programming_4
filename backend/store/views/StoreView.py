from rest_framework.decorators import action
from store.views.BaseView import BaseViewSet
from store.serializers import StoreSerializer
from store.repositories.unit_of_work import UnitOfWork
from rest_framework.response import Response

uow = UnitOfWork()

class StoreViewSet(BaseViewSet):
    repo = uow.stores
    serializer_class = StoreSerializer

    @action(detail=False, methods=['get'])
    def by_city(self, request):
        city = request.query_params.get('city')
        if not city:
            return Response({'error': 'city parameter required'}, status=400)
        stores = uow.stores.get_by_city(city)
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_email(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({'error': 'email parameter required'}, status=400)
        stores = uow.stores.find_by_email(email)
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)