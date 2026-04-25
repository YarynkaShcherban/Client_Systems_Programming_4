from rest_framework.decorators import action
from store.views.BaseView import BaseViewSet
from store.serializers import PublisherSerializer
from store.repositories.unit_of_work import UnitOfWork
from rest_framework.response import Response

uow = UnitOfWork()

class PublisherViewSet(BaseViewSet):
    repo = uow.publishers
    serializer_class = PublisherSerializer

    @action(detail=False, methods=['get'])
    def by_email(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({'error': 'email parameter required'}, status=400)
        publishers = uow.publishers.find_by_email(email)
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data)