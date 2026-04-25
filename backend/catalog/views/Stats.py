from django.shortcuts import render, redirect
from ..ApiManager import *
from store.repositories.BookRepo import BookRepo
from store.repositories.GenreRepo import GenreRepo
from store.repositories.PublisherRepo import PublisherRepo
import pandas as pd
import plotly.express as px
from store.repositories.StatsRepo import StatsRepo
from django.http import JsonResponse

book_repo = BookRepo()
genre_repo = GenreRepo()
publisher_repo = PublisherRepo()


def get_book_stats():
    stats = {
        "overall": {},
        "genres": [],
        "publishers": [],
    }

    overall = book_api.client.get("catalog/books/stats/overall/")
    if isinstance(overall, dict) and not overall.get("error"):
        stats["overall"] = overall
    else:
        stats["overall"] = {"avg_price": 0, "total_books": 0}

    genres = genre_api.client.get("catalog/genres/stats/")
    if isinstance(genres, list):
        stats["genres"] = genres

    publishers = publisher_api.client.get("catalog/publishers/stats/")
    if isinstance(publishers, list):
        stats["publishers"] = publishers
    return stats


def book_stats(request):
    try:
        stats = get_book_stats()
        try:
            books = book_api.get_all_books()
        except Exception as ex_books:
            print("Помилка завантаження books через API:", ex_books)
            books = []

        return render(request, "catalog/stats.html", {
            "stats": stats,
            "books": books,
        })
    except Exception as ex:
        print("Помилка stats:", ex)
        return render(request, "errors/500.html", status=500)
    
def avg_price_by_genre_store(request):
    genre = request.GET.get("genre", "")
    data_queryset = list(StatsRepo.avg_price_by_genre_and_store())
    df = pd.DataFrame(data_queryset)

    available_genres = df['genre_name'].unique(
    ).tolist() if not df.empty else []

    if not genre and available_genres:
        genre = available_genres[0]
    if genre and genre in available_genres:
        filtered_df = df[df['genre_name'] == genre]
    else:
        filtered_df = pd.DataFrame()

    if not filtered_df.empty:
        filtered_df = filtered_df.sort_values('avg_price', ascending=False)
        fig = px.line(
            filtered_df,
            x='store_name',
            y='avg_price',
            markers=True,
            labels={'store_name': 'Магазин', 'avg_price': 'Середня ціна, грн'},
            template='plotly_white'
        )
        fig.update_layout(
            xaxis={'categoryorder': 'total descending', 'tickangle': 20},
            yaxis={'rangemode': 'tozero'}
        )
        fig.update_traces(line_color='#f4a259')
        graph_json = fig.to_json()
    else:
        graph_json = "{}"

    return JsonResponse({
        'graph_json': graph_json,
        'available_genres': available_genres,
        'current_genre': genre
    })

def get_main_stats():
    genres = genre_api.get_all_genres()
    all_stats = []
    for g in genres:
        genre_id = g['genre_id']
        books = book_api.get_books_by_genre(genre_id)
        prices = []
        for b in books:
            price = float(b.get('price'))
            prices.append(price)

        if prices:
            stats = {
                'price': prices,
                'genre': g['name'],
                'avg_price': round(sum(prices)/len(prices), 2),
                'median_price': round(pd.Series(prices).median(), 2),
                'min_price': min(prices),
                'max_price': max(prices)
            }
            all_stats.append(stats)
    return pd.DataFrame(all_stats)