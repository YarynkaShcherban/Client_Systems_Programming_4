from django.http import JsonResponse
from django.views import View
from store.repositories.StatsRepo import StatsRepo

class StatsViewSet(View):
    def get_book_overall_stats(self, request):
        data = StatsRepo.book_overall_stats()
        return JsonResponse(data, safe=False)

    def get_genre_stats(self, request):
        data = StatsRepo.genre_stats()
        return JsonResponse(data, safe=False)

    def get_publisher_stats(self, request):
        data = StatsRepo.publisher_stats()
        return JsonResponse(data, safe=False)