from rest_framework.decorators import action
from store.views.BaseView import BaseViewSet
from store.serializers import AuthorSerializer
from store.repositories.unit_of_work import UnitOfWork
from rest_framework.response import Response

uow = UnitOfWork()

class AuthorViewSet(BaseViewSet):
    repo = uow.authors
    serializer_class = AuthorSerializer

    @action(detail=False, methods=['get'])
    def search_by_last_name(self, request):
        last_name = request.query_params.get('last_name')
        if not last_name:
            return Response({'error': 'last_name parameter required'}, status=400)
        authors = self.repo.find_by_last_name(last_name)
        serializer = self.serializer_class(authors, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def alive(self, request):
        authors = self.repo.get_alive_authors()
        serializer = self.serializer_class(authors, many=True)
        return Response(serializer.data)