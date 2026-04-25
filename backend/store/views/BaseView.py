from rest_framework import viewsets, status
from rest_framework.response import Response


class BaseViewSet(viewsets.ViewSet):
    repo = None
    serializer_class = None
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def list(self, request):
        queryset = self.repo.get_all()
        publisher_id = request.query_params.get("publisher")
        genre_id = request.query_params.get("genre")

        if publisher_id:
            queryset = queryset.filter(publisher_id=publisher_id)
        if genre_id:
            queryset = queryset.filter(genres__genre_id=genre_id)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = self.repo.get_by_id(pk)
        if not item:
            return Response({'error': f'{self.serializer_class.Meta.model.__name__} not found'}, status=404)
        serializer = self.serializer_class(item)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            item = self.repo.create(**serializer.validated_data)
            return Response(self.serializer_class(item).data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        item = self.repo.get_by_id(pk)
        if not item:
            return Response({'error': f'{self.serializer_class.Meta.model.__name__} not found'}, status=404)
        serializer = self.serializer_class(item, data=request.data)
        if serializer.is_valid():
            updated_item = self.repo.update(pk, **serializer.validated_data)
            return Response(self.serializer_class(updated_item).data)
        return Response(serializer.errors, status=400)
    
    def partial_update(self, request, pk=None):
        item = self.repo.get_by_id(pk)
        if not item:
            return Response({'error': f'{self.serializer_class.Meta.model.__name__} not found'}, status=404)
    
        serializer = self.serializer_class(item, data=request.data, partial=True)  # partial=True для PATCH
        if serializer.is_valid():
            updated_item = self.repo.update(pk, **serializer.validated_data)
            return Response(self.serializer_class(updated_item).data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        deleted = self.repo.delete(pk)
        if not deleted:
            return Response({'error': f'{self.serializer_class.Meta.model.__name__} not found'}, status=404)
        return Response(status=204)