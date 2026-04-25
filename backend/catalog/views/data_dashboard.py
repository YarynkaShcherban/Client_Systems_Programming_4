import pandas as pd
from store.repositories.StatsRepo import StatsRepo
from catalog.views.Stats import *
from django.db.models import Avg
from store.models import Book
from ..ApiManager import *
from store.repositories.StatsRepo import StatsRepo
import time
from concurrent.futures import ThreadPoolExecutor


def get_main_stats_df():
    return get_main_stats()

def get_genres_stats_df():
    data = list(StatsRepo.genres_with_books_and_avg_price())
    df = pd.DataFrame(data, columns=['name', 'num_books', 'avg_price'] if data else [])
    if not df.empty:
        df['avg_price'] = df['avg_price'].astype(float)
    return df

def get_authors_stats_df():
    data = list(StatsRepo.authors_avg_book_price())
    df = pd.DataFrame(data, columns=['first_name', 'last_name', 'avg_price'] if data else [])
    if not df.empty:
        df['avg_price'] = df['avg_price'].astype(float)
        df['full_name'] = df['first_name'] + ' ' + df['last_name']
    return df

def get_top_authors_df():
    data = list(StatsRepo.top_authors_by_book_count())
    df = pd.DataFrame(data, columns=['first_name', 'last_name', 'num_books'] if data else [])
    if not df.empty:
        df['full_name'] = df['first_name'] + ' ' + df['last_name']
    return df

def get_publishers_stats_df():
    data = list(StatsRepo.publishers_avg_price())
    df = pd.DataFrame(data, columns=['name', 'num_books', 'avg_price'] if data else [])
    if not df.empty:
        df['avg_price'] = df['avg_price'].astype(float)
    return df

def get_expensive_publishers_df():
    data = list(StatsRepo.expensive_publishers())
    df = pd.DataFrame(data, columns=['name', 'avg_price'] if data else [])
    if not df.empty:
        df['avg_price'] = df['avg_price'].astype(float)
    return df

def get_store_stats_df():
    data = list(StatsRepo.store_sales_stats())
    df = pd.DataFrame(data, columns=['name', 'total_sales', 'total_purchases'] if data else [])
    if not df.empty:
        df['total_sales'] = df['total_sales'].astype(float)
    return df


class BenchmarkManager:
    @staticmethod
    def get_segment_avg(chunk_ids):
        return Book.objects.filter(book_id__in=chunk_ids).aggregate(Avg('price'))['price__avg'] or 0

    @staticmethod
    def run_thread_test():
        all_ids = list(Book.objects.values_list('book_id', flat=True))
        test_threads = [1, 2, 4, 8, 16, 32, 64, 128, 256]
        async_results = []

        for n in test_threads:
            chunk_size = max(1, len(all_ids) // n)
            chunks = [all_ids[i:i + chunk_size] for i in range(0, len(all_ids), chunk_size)]
            start_time = time.time()
            with ThreadPoolExecutor(max_workers=n) as executor:
                list(executor.map(BenchmarkManager.get_segment_avg, chunks))
            async_results.append({
                'threads': n, 
                'execution_time': time.time() - start_time
            })
        return pd.DataFrame(async_results)