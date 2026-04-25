from django.shortcuts import render
from plotly.offline import plot
from store.repositories.StatsRepo import StatsRepo
from store.views.benchmark_service import BenchmarkService
from catalog.views.dashboard_service import get_dashboard_figures
from catalog.views.charts_factory import create_benchmark_line_chart
from catalog.views.data_dashboard import *

def benchmark_view(request):
    try:
        df_200 = BenchmarkService.get_benchmark_data(n_requests=200)
        df_500 = BenchmarkService.get_benchmark_data(n_requests=500)
        df_10000 = BenchmarkService.get_benchmark_data(n_requests=10000)
        df_async = BenchmarkManager.run_thread_test()

        def get_opt(df, time_col):
            row = df.loc[df[time_col].idxmin()]
            return {'threads': int(row['threads']), 'time': round(row[time_col], 4)}
        
        fig_200 = create_benchmark_line_chart(df_200, "Результати для 200 запитів")
        fig_500 = create_benchmark_line_chart(df_500, "Результати для 500 запитів", color='#ef476f')
        fig_10000 = create_benchmark_line_chart(df_10000, "Навантаження: 10 000 запитів", color='#8B5CF6')
        fig_async = create_benchmark_line_chart(df_async, "Вплив кількості потоків", color='#00CC96', y_col='execution_time')

        return render(request, 'catalog/benchmark.html', {
            'graph_200': plot(fig_200, output_type='div'),
            'graph_500': plot(fig_500, output_type='div'),
            'graph_10000': plot(fig_10000, output_type='div'),
            'graph_div': plot(fig_async, output_type='div'),
            
            'opt_200': get_opt(df_200, 'total_time'),
            'opt_500': get_opt(df_500, 'total_time'),
            'opt_10000': get_opt(df_10000, 'total_time'),
            
            'table_200': df_200.to_dict('records'),
            'table_500': df_500.to_dict('records'),
            'table_10000': df_10000.to_dict('records'),
            'table_data': df_async.to_dict('records'),
            
            'optimal_threads': get_opt(df_async, 'execution_time')['threads'],
            'min_time': get_opt(df_async, 'execution_time')['time'],
        })
    except Exception as e:
        return render(request, "errors/500.html", {"error": str(e)}, status=500)


def dashboard_page(request):
    try:
        context = get_dashboard_figures()
        return render(request, 'catalog/dashboard.html', context)
    except Exception as e:
        print(e)
        return render(request, 'errors/500.html', status=500)