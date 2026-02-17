"""Tests for sorting.py"""

import unittest
import sys
import pandas as pd
sys.path.append('.')
from src.sorting import CaseSorter

class TestCaseSorter(unittest.TestCase):
    """Tests for the CaseSorter class."""
    
    def setUp(self) -> None:
        """Load the Boston dataset and initialize CaseSorter."""
        df = pd.read_csv("data/311_Cases_Boston.csv")
        self.sorter = CaseSorter(df)

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
        ranking = self.sorter.create_urgency_ranking()
        result = self.sorter.sort_by_urgency(ranking)

        first_score = result.iloc[0]["urgency_score"]
        second_score = result.iloc[1]["urgency_score"]

        self.assertGreaterEqual(first_score, second_score)

    def test_sort_by_urgency_empty_ranking(self) -> None:
        """Test that sort_by_urgency raises ValueError when ranking is empty."""
        with self.assertRaises(ValueError):
            self.sorter.sort_by_urgency({})

    def test_constructor_missing_column(self) -> None:
        """Test that constructor raises KeyError if required column missing."""
        df = pd.read_csv("data/311_Cases_Boston.csv")
        df = df.drop(columns=["CaseID"])

        with self.assertRaises(KeyError):
            CaseSorter(df)
    
    def test_sort_by_urgency_no_overlap(self) -> None:
        """Test that sort_by_urgency raises ValueError if no categories overlap."""
        ranking = {"Fake Category": 100}

        with self.assertRaises(ValueError):
            self.sorter.sort_by_urgency(ranking)

