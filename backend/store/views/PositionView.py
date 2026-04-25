from rest_framework.decorators import action
from store.views.BaseView import BaseViewSet
from store.serializers import PositionSerializer
from store.repositories.unit_of_work import UnitOfWork
from rest_framework.response import Response

uow = UnitOfWork()

class PositionViewSet(BaseViewSet):
    repo = uow.positions
    serializer_class = PositionSerializer

    @action(detail=False, methods=['get'])
    def by_role(self, request):
        role = request.query_params.get('role')
        if not role:
            return Response({'error': 'role parameter required'}, status=400)
        positions = uow.positions.find_by_role(role)
        serializer = PositionSerializer(positions, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def salary_range(self, request):
        min_salary = request.query_params.get('min_salary')
        max_salary = request.query_params.get('max_salary')
        if min_salary is None or max_salary is None:
            return Response({'error': 'min_salary and max_salary required'}, status=400)
        positions = uow.positions.get_salary_range(min_salary, max_salary)
        serializer = PositionSerializer(positions, many=True)
        return Response(serializer.data)