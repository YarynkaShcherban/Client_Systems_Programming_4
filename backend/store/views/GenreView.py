from rest_framework.decorators import action
from store.views.BaseView import BaseViewSet
from store.serializers import GenreSerializer
from store.repositories.unit_of_work import UnitOfWork
from rest_framework.response import Response

uow = UnitOfWork()

class GenreViewSet(BaseViewSet):
    repo = uow.genres
    serializer_class = GenreSerializer

    @action(detail=False, methods=['get'])
    def search_by_name(self, request):
        name = request.query_params.get('name')
        if not name:
            return Response({'error': 'name parameter required'}, status=400)
        genres = uow.genres.find_by_name(name)
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
