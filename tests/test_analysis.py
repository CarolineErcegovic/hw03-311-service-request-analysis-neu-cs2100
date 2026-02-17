"""Tests for analysis.py"""

import unittest
import sys
import pandas as pd
sys.path.append('.')
from src.analysis import Analyzer

class TestAnalyzer(unittest.TestCase):
    """Tests for the Analyzer class."""
    def setUp(self) -> None:
        """Load the Boston dataset and initialize Analyzer."""
        df = pd.read_csv("data/311_Cases_Boston.csv")
        self.analyzer = Analyzer(df)

    def test_average_days_open(self) -> None:
        """Test that average_days_open returns a float greater than or equal to 0."""
        result = self.analyzer.average_days_open()

        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0)

    def test_cases_per_neighborhood(self) -> None:
        """Test that cases_per_neighborhood returns a non-empty dictionary."""
        result = self.analyzer.cases_per_neighborhood()

        self.assertIsInstance(result, dict)
        self.assertGreater(len(result), 0)

    def test_cases_above_average_per_neighborhood(self) -> None:
        """Test that cases_above_average_per_neighborhood returns valid counts."""
        result = self.analyzer.cases_above_average_per_neighborhood()

        self.assertIsInstance(result, dict)
        self.assertGreater(len(result), 0)

        for value in result.values():
            self.assertGreaterEqual(value, 0)

    def test_percentage_above_average_per_neighborhood(self) -> None:
        """Test that percentage_above_average_per_neighborhood 
        returns percentages between 0 and 100."""
        result = self.analyzer.percentage_above_average_per_neighborhood()

        self.assertIsInstance(result, dict)
        self.assertGreater(len(result), 0)

        for value in result.values():
            self.assertGreaterEqual(value, 0)
            self.assertLessEqual(value, 100)
    
    def test_constructor_missing_column(self) -> None:
        """Test that Analyzer constructor raises KeyError if required column missing."""
        df = pd.read_csv("data/311_Cases_Boston.csv")
        df = df.drop(columns=["CaseID"])

        with self.assertRaises(KeyError):
            Analyzer(df)

    def test_average_days_open_empty_dataset(self) -> None:
        """Test average_days_open on empty dataset."""
        df = pd.DataFrame(columns=self.analyzer.df.columns)
        analyzer = Analyzer(df)

        result = analyzer.average_days_open()

        self.assertTrue(pd.isna(result) or result == 0)
    
    def test_average_days_open_nonnumeric(self) -> None:
        """Test average_days_open with nonnumeric days_open."""
        df = pd.read_csv("data/311_Cases_Boston.csv")
        df["days_open"] = "not a number"

        analyzer = Analyzer(df)

        with self.assertRaises(Exception):
            analyzer.average_days_open()

