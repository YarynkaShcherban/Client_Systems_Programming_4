import sys
import logging
from unittest.mock import patch, MagicMock
from io import BytesIO
from django.test import SimpleTestCase
import pandas as pd
from bokeh.plotting import figure
from catalog.views.charts_factory import *

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    stream=sys.stdout
)

class TestChartsFactory(SimpleTestCase):
    def setUp(self):
        self.df_genres = pd.DataFrame({
            'name': ['Фентезі', 'Детектив', 'Наукова'],
            'num_books': [10, 5, 8],
            'avg_price': [200, 150, 300]
        })

        self.df_authors = pd.DataFrame({
            'first_name': ['Іван', 'Петро'],
            'last_name': ['Іваненко', 'Петренко'],
            'avg_price': [180, 220]
        })
        self.df_authors['full_name'] = self.df_authors['first_name'] + ' ' + self.df_authors['last_name']
        self.df_empty = pd.DataFrame()


    def test_create_main_stats_plotly_returns_figure(self):
        df = pd.DataFrame({
            'genre': ['Жанр1', 'Жанр2'],
            'avg_price': [100, 200],
            'median_price': [90, 190],
            'min_price': [80, 180],
            'max_price': [110, 210]
        })
        fig = create_main_stats_plotly(df)
        self.assertIsNotNone(fig)
        self.assertEqual(len(fig.data), 4)  # 4 бари
        logger.info("Тест : create_main_stats_plotly – фігура створена.")


    def test_create_main_stats_plotly_empty_returns_none(self):
        self.assertIsNone(create_main_stats_plotly(self.df_empty))
        self.assertIsNone(create_main_stats_plotly(None))
        logger.info("Тест : create_main_stats_plotly – повертає None для пустого або None DataFrame.")


    def test_create_genres_count_plotly_colors_and_sorting(self):
        fig = create_genres_count_plotly(self.df_genres)
        self.assertIsNotNone(fig)
        self.assertEqual(fig.data[0].marker.color, '#8ECAE6')
        self.assertEqual(list(fig.data[0].x), ['Фентезі', 'Наукова', 'Детектив'])
        logger.info("Тест : create_genres_count_plotly – колір та сортування перевірено.")


    def test_apply_bokeh_styles_changes_font_size_and_style(self):
        p = figure()
        styled = apply_bokeh_styles(p)
        self.assertEqual(styled.xaxis.axis_label_text_font_size, "12pt")
        self.assertEqual(styled.xaxis.axis_label_text_font_style, "bold")
        logger.info("Тест : apply_bokeh_styles – шрифт і стиль підписів застосовано правильно.")


    def test_create_genres_count_bokeh_returns_figure(self):
        p = create_genres_count_bokeh(self.df_genres)
        self.assertIsInstance(p, figure)
        self.assertEqual(p.xaxis.axis_label, "Жанр")
        self.assertEqual(p.yaxis.axis_label, "Кількість книг")
        logger.info("Тест : create_genres_count_bokeh – Bokeh фігура створена з правильними підписами.")


    def test_create_genres_count_bokeh_empty_returns_none(self):
        self.assertIsNone(create_genres_count_bokeh(self.df_empty))
        self.assertIsNone(create_genres_count_bokeh(None))
        logger.info("Тест : create_genres_count_bokeh – повертає None для пустого або None DataFrame.")


    def test_create_authors_price_bokeh_sets_correct_color(self):
        p = create_authors_price_bokeh(self.df_authors)
        glyph = p.renderers[0].glyph
        self.assertEqual(glyph.fill_color, "#f4a259")
        logger.info("Тест : create_authors_price_bokeh – колір встановлено правильно.")


    def test_create_benchmark_line_chart_returns_figure(self):
        df = pd.DataFrame({
            'threads': [1, 2, 4],
            'total_time': [0.5, 0.3, 0.25]
        })
        fig = create_benchmark_line_chart(df, "Test Chart")
        self.assertIsNotNone(fig)
        self.assertEqual(fig.data[0].line.color, '#2196f3')
        logger.info("Тест : create_benchmark_line_chart – фігура створена з правильним кольором лінії.")


    def test_create_benchmark_line_chart_empty_returns_none(self):
        self.assertIsNone(create_benchmark_line_chart(self.df_empty, "Empty Chart"))
        self.assertIsNone(create_benchmark_line_chart(None, "Empty Chart"))
        logger.info("Тест : create_benchmark_line_chart – повертає None для пустого або None DataFrame.")