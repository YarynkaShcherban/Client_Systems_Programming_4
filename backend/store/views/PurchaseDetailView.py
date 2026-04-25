from rest_framework.decorators import action
from store.views.BaseView import BaseViewSet
from store.serializers import PurchaseDetailSerializer
from store.repositories.unit_of_work import UnitOfWork
from rest_framework.response import Response

uow = UnitOfWork()

class PurchaseDetailViewSet(BaseViewSet):
    repo = uow.purchase_details
    serializer_class = PurchaseDetailSerializer

    @action(detail=False, methods=['get'])
    def by_purchase(self, request):
        purchase_id = request.query_params.get('purchase_id')
        if not purchase_id:
            return Response({'error': 'purchase_id required'}, status=400)
        details = uow.purchase_details.get_by_purchase(purchase_id)
        serializer = PurchaseDetailSerializer(details, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def total_sum(self, request):
        purchase_id = request.query_params.get('purchase_id')
        if not purchase_id:
            return Response({'error': 'purchase_id required'}, status=400)
        total = uow.purchase_details.get_total_sum_by_purchase(purchase_id)
        return Response({'total_sum': total})