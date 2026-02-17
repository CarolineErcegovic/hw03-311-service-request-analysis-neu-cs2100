"""Tests for analysis.py"""

import unittest
import sys
import pandas as pd
sys.path.append('.')
from src.analysis import Analyzer

def make_test_dataframe() -> pd.DataFrame:
    """Create a small valid DataFrame for testing."""
    return pd.DataFrame({
        "CaseID": [1, 2, 3, 4],
        "Status": ["Open", "Closed", "Open", "Closed"],
        "Category": ["A", "B", "A", "B"],
        "Street": ["X", "Y", "Z", "W"],
        "Supervisor District": [1, 1, 2, 2],
        "Neighborhood": ["N1", "N1", "N2", "N2"],
        "Police District": ["P1", "P1", "P2", "P2"],
        "Latitude": [1.0, 2.0, 3.0, 4.0],
        "Longitude": [4.0, 5.0, 6.0, 7.0],
        "Point": ["", "", "", ""],
        "point_geom": ["", "", "", ""],
        "OpenedDate": ["", "", "", ""],
        "ClosedDate": ["", "", "", ""],
        "days_open": [5, 10, 3, 7],
        "selected": [False, False, False, False]
    })

class TestAnalyzer(unittest.TestCase):
    """Tests for the Analyzer class."""
    def setUp(self) -> None:
        """Load the Boston dataset and initialize Analyzer."""
        self.df = make_test_dataframe()
        self.analyzer = Analyzer(self.df)

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
        df_bad = make_test_dataframe().drop(columns=["CaseID"])
        with self.assertRaises(KeyError):
            Analyzer(df_bad)

    def test_average_days_open_empty_dataset(self) -> None:
        """Test average_days_open on empty dataset."""
        df = pd.DataFrame(columns=self.analyzer.df.columns)
        analyzer = Analyzer(df)

        result = analyzer.average_days_open()

        self.assertTrue(pd.isna(result) or result == 0)
    
    def test_average_days_open_nonnumeric(self) -> None:
        """Test average_days_open with nonnumeric days_open."""
        df_bad = make_test_dataframe()
        df_bad["days_open"] = ["a", "b", "c", "d"]

        analyzer = Analyzer(df_bad)

        with self.assertRaises(Exception):
            analyzer.average_days_open()