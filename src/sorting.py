"""
Module responsible for sorting 311 cases and managing urgency rankings.
Combines sorting and urgency functions as they work together conceptually.
"""

import pandas as pd
import numpy as np


REQUIRED_COLUMNS = [
    'CaseID', 'Status', 'Category', 'Street', 'Supervisor District',
    'Neighborhood', 'Police District', 'Latitude', 'Longitude', 'Point',
    'point_geom', 'OpenedDate', 'ClosedDate', 'days_open', 'selected'
]

class CaseSorter:
    """
    Class for sorting and ranking 311 cases.
    """

    def __init__(self, df: pd.DataFrame, required_columns: list[str] = REQUIRED_COLUMNS) -> None:
        """
        Initialize with the 311 cases dataset.

        Args:
            df (pd.DataFrame): The 311 cases dataset
            required_columns (list[str]): List of required columns in the DataFrame

        Raises:
            KeyError: If the DataFrame is missing any of the required columns.
        """
    
        self.df = df
        for col in required_columns:
            if col not in df.columns:
                raise KeyError("Not all of the required columns are in the data frame.")


    def sort_by_days_open(self,  ascending: bool = False, days_open_column: str = "days_open") -> pd.DataFrame:
        """
        Return dataset of 311 cases sorted by how long they were open.
        
        Args:
            ascending (bool): If True, sort from shortest to longest duration
            days_open_column (str): The column name for days open. Default: "days_open"
            
        Returns:
            pd.DataFrame: Sorted dataset
        """
        sorted_df = self.df.sort_values(by= days_open_column, ascending = ascending) 

        return sorted_df
        

    def create_urgency_ranking(self) -> dict[str, int]:
        """
        Determine appropriate urgency rankings for each 311 case category.
            
        Returns:
            dict[str, int]: Dictionary mapping categories to urgency scores 
                           (lower = less urgent, higher = more urgent)
                                   """
        
        return {"Request for Pothole Repair": 500, 
                "Pick up Dead Animal" : 400, 
                "Missing Sign" :350, 
                "Pest Infestation - Residential": 300,
                "Animal Generic Request": 275,
                "Requests for Street Cleaning" : 250,
                "Traffic Signal Inspection": 225,
                "Recycling Cart Return": 200,
                "Parking Enforcement": 100,
                "Poor Conditions of Property": 50
                }
        

    def sort_by_urgency(self, urgency_ranking: dict[str, int], category_column: str = "Category") -> pd.DataFrame:
        """
        Return a filtered version of the dataset including only the categories 
        that have been ranked, sorted by urgency ranking, descending (so more urgent
        cases are earlier).
        
        Args:
            urgency_ranking (dict[str, int]): Dictionary mapping categories to urgency scores,
                where a higher urgency score is more urgent
            category_column (str): The column name for categories. Default: "Category".
            
        Returns:
            pd.DataFrame: Dataset sorted by urgency (most urgent first).
                Ties are broken using days_open, descending (so more days is more urgent).
            
        Raises:
            ValueError: If urgency_ranking is empty
            ValueError: If no categories in the dataset are found in urgency_ranking
            ValueError: If no categories in urgency_ranking are found in the dataset
        """

        if not urgency_ranking:
            raise ValueError("urgency_ranking cannot be empty.")

        dataset_categories = set(self.df[category_column])
        ranking_categories = set(urgency_ranking.keys())

        if dataset_categories.isdisjoint(ranking_categories):
            raise ValueError("No categories in the dataset are found in urgency_ranking.")

        if ranking_categories.isdisjoint(dataset_categories):
            raise ValueError("No categories in urgency_ranking are found in the dataset.")

        filtered_df = self.df[self.df[category_column].isin(urgency_ranking)].copy()

        filtered_df["urgency_score"] = filtered_df[category_column].map(urgency_ranking)

        sorted_df = filtered_df.sort_values(
            by=["urgency_score", "days_open"],
            ascending=[False, False]
        )

        return sorted_df
