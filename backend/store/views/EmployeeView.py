from rest_framework.decorators import action
from store.views.BaseView import BaseViewSet
from store.serializers import EmployeeSerializer
from store.repositories.unit_of_work import UnitOfWork
from rest_framework.response import Response

uow = UnitOfWork()

class EmployeeViewSet(BaseViewSet):
    repo = uow.employees
    serializer_class = EmployeeSerializer

    @action(detail=False, methods=['get'])
    def by_last_name(self, request):
        last_name = request.query_params.get('last_name')
        if not last_name:
            return Response({'error': 'last_name parameter required'}, status=400)
        employees = uow.employees.find_by_last_name(last_name)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_position(self, request):
        role = request.query_params.get('role')
        if not role:
            return Response({'error': 'role parameter required'}, status=400)
        employees = uow.employees.get_by_position(role)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_store(self, request):
        store_id = request.query_params.get('store_id')
        if not store_id:
            return Response({'error': 'store_id parameter required'}, status=400)
        employees = uow.employees.get_by_store(store_id)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)