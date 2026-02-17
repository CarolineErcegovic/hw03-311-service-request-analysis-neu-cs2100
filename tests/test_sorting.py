"""Tests for sorting.py"""

import unittest
import sys
import pandas as pd
sys.path.append('.')
from src.sorting import CaseSorter

def make_test_dataframe() -> pd.DataFrame:
    """Create a small valid DataFrame for testing."""
    return pd.DataFrame({
        "CaseID": [1, 2, 3],
        "Status": ["Open", "Closed", "Open"],
        "Category": ["A", "B", "A"],
        "Street": ["X", "Y", "Z"],
        "Supervisor District": [1, 1, 2],
        "Neighborhood": ["N1", "N1", "N2"],
        "Police District": ["P1", "P1", "P2"],
        "Latitude": [1.0, 2.0, 3.0],
        "Longitude": [4.0, 5.0, 6.0],
        "Point": ["", "", ""],
        "point_geom": ["", "", ""],
        "OpenedDate": ["", "", ""],
        "ClosedDate": ["", "", ""],
        "days_open": [5, 10, 3],
        "selected": [False, False, False]
    })

class TestCaseSorter(unittest.TestCase):
    """Tests for the CaseSorter class."""
    
    def setUp(self) -> None:
        """Load the Boston dataset and initialize CaseSorter."""
        self.df = make_test_dataframe()
        self.sorter = CaseSorter(self.df)

    def test_sort_by_days_open_descending(self) -> None:
        """Test that sort_by_days_open sorts from longest to shortest by default."""
        result = self.sorter.sort_by_days_open()

        first_value = result.iloc[0]["days_open"]
        second_value = result.iloc[1]["days_open"]

        self.assertGreaterEqual(first_value, second_value)

    def test_sort_by_days_open_ascending(self) -> None:
        """Test that sort_by_days_open sorts from shortest to longest when ascending=True."""
        result = self.sorter.sort_by_days_open(ascending=True)

        first_value = result.iloc[0]["days_open"]
        second_value = result.iloc[1]["days_open"]

        self.assertLessEqual(first_value, second_value)

    def test_create_urgency_ranking(self) -> None:
        """Test that create_urgency_ranking returns a dictionary with at least 10 categories."""
        ranking = self.sorter.create_urgency_ranking()

        self.assertIsInstance(ranking, dict)
        self.assertGreaterEqual(len(ranking), 10)

    def test_sort_by_urgency(self) -> None:
        """Test that sort_by_urgency sorts by urgency score descending."""
        ranking = {"A": 200, "B": 100}
        result = self.sorter.sort_by_urgency(ranking)

        self.assertEqual(result.iloc[0]["Category"], "A")

    def test_sort_by_urgency_empty_ranking(self) -> None:
        """Test that sort_by_urgency raises ValueError when ranking is empty."""
        with self.assertRaises(ValueError):
            self.sorter.sort_by_urgency({})

    def test_constructor_missing_column(self) -> None:
        """Test that constructor raises KeyError if required column missing."""
        df_bad = make_test_dataframe().drop(columns=["CaseID"])

        with self.assertRaises(KeyError):
            CaseSorter(df_bad)
    
    def test_sort_by_urgency_no_overlap(self) -> None:
        """Test that sort_by_urgency raises ValueError if no categories overlap."""
        ranking = {"Fake Category": 100}

        with self.assertRaises(ValueError):
            self.sorter.sort_by_urgency(ranking)
