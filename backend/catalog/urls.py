from django.urls import path
from .views.book import *
from .views.dashboard import *
from .views.StatsView import *

stats_view = StatsViewSet()
app_name = "catalog"

urlpatterns = [
    path('', book_list, name='book_list'),
    path('create/', book_create, name='book_create'),
    path('genre/<int:genre_id>/', book_list_by_genre, name='book_list_by_genre'),
    path('publisher/<int:publisher_id>/',
         book_list_by_publisher, name='book_list_by_publisher'),
    path('<int:book_id>/edit/', book_update, name='book_update'),
    path('<int:book_id>/delete/', book_delete, name='book_delete'),
    path('<int:book_id>/details/', book_detail, name='book_detail'),
    path('stats/', book_stats, name='book_stats'),
    path('dashboard/page/', dashboard_page, name='dashboard_page'),
    path('benchmark/', benchmark_view, name='benchmark_page'),
    path("books/stats/overall/", stats_view.get_book_overall_stats,
         name="stats_books_overall"),
    path("genres/stats/", stats_view.get_genre_stats, name="stats_genres"),
    path("publishers/stats/", stats_view.get_publisher_stats,
         name="stats_publishers"),
    path('avg-price-by-genre-store/', avg_price_by_genre_store,
         name='avg_price_by_genre_store'),
]