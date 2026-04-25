import time
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

class BenchmarkService:
    @staticmethod
    def single_request(url):
        try:
            from catalog.ApiManager import BookApiManager
            return BookApiManager.client.get(url)
        except:
            return None

    @staticmethod
    def run_experiment(n_requests, n_workers):
        url = "catalog/books/stats/overall/"
        urls = [url] * n_requests
        start_time = time.time()

        with ThreadPoolExecutor(max_workers=n_workers) as executor:
            list(executor.map(BenchmarkService.single_request, urls))

        return time.time() - start_time

    @staticmethod
    def get_benchmark_data(n_requests):
        results = []
        worker_counts = [1, 2, 4, 8, 16, 32, 64] 
        
        for workers in worker_counts:
            duration = BenchmarkService.run_experiment(n_requests, workers)
            results.append({
                'threads': workers,
                'total_time': duration,
                'throughput': n_requests / duration  
            })
        return pd.DataFrame(results)