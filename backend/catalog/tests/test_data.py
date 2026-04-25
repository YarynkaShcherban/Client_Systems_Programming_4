import logging
import sys
import pandas as pd
from unittest.mock import patch
from django.test import SimpleTestCase
from catalog.views.data_dashboard import get_genres_stats_df, get_authors_stats_df

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    stream=sys.stdout
)

class TestDashboardLogic(SimpleTestCase):
    @patch('store.repositories.StatsRepo.StatsRepo.genres_with_books_and_avg_price')
    def test_genres_dataframe_transformation(self, mock_repo):
        mock_repo.return_value = [
            {'name': 'Sci-Fi', 'num_books': 10, 'avg_price': 250.50},
            {'name': 'Drama', 'num_books': 5, 'avg_price': 100.00},
        ]

        df = get_genres_stats_df()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertListEqual(list(df.columns), ['name', 'num_books', 'avg_price'])
        self.assertIsInstance(df['avg_price'].iloc[0], float)

        df_sorted = df.sort_values('avg_price', ascending=False)
        self.assertEqual(df_sorted.iloc[0]['name'], 'Sci-Fi')
        logger.info("Тест : Трансформація та типізація DataFrame для жанрів пройшла успішно.")


    @patch('store.repositories.StatsRepo.StatsRepo.authors_avg_book_price')
    def test_authors_full_name_logic(self, mock_repo):
        mock_repo.return_value = [{'first_name': 'Taras', 'last_name': 'Shevchenko', 'avg_price': 500}]
        
        df = get_authors_stats_df()
        self.assertEqual(df.iloc[0]['full_name'], 'Taras Shevchenko')
        logger.info("Тест : Логіка формування full_name працює.")


    def test_edge_cases_empty_and_none(self):
        with patch('store.repositories.StatsRepo.StatsRepo.genres_with_books_and_avg_price', return_value=[]):
            df = get_genres_stats_df()
            self.assertTrue(df.empty)
            
        logger.info("Тест : Порожній список у статистиці оброблено коректно.")