from rest_framework.decorators import action
from store.views.BaseView import BaseViewSet
from store.serializers import PurchaseSerializer
from store.repositories.unit_of_work import UnitOfWork
from rest_framework.response import Response

uow = UnitOfWork()

class PurchaseViewSet(BaseViewSet):
    repo = uow.purchases
    serializer_class = PurchaseSerializer

    @action(detail=False, methods=['get'])
    def by_client(self, request):
        client_id = request.query_params.get('client_id')
        if not client_id:
            return Response({'error': 'client_id required'}, status=400)
        purchases = uow.purchases.get_by_client(client_id)
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_employee(self, request):
        employee_id = request.query_params.get('employee_id')
        if not employee_id:
            return Response({'error': 'employee_id required'}, status=400)
        purchases = uow.purchases.get_by_employee(employee_id)
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_store(self, request):
        store_id = request.query_params.get('store_id')
        if not store_id:
            return Response({'error': 'store_id required'}, status=400)
        purchases = uow.purchases.get_by_store(store_id)
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_date_range(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        if not start_date or not end_date:
            return Response({'error': 'start_date and end_date required'}, status=400)
        purchases = uow.purchases.get_by_date_range(start_date, end_date)
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data)