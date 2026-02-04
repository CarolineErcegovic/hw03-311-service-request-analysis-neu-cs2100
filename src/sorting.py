"""
Module responsible for sorting 311 cases and managing urgency rankings.
Combines sorting and urgency functions as they work together conceptually.
"""

import pandas as pd

class CaseSorter:
    """
    Class for sorting and ranking 311 cases.
    """

    def __init__(self, df: pd.DataFrame) -> None:
        """
        Initialize with the 311 cases dataset.

        Args:
            df (pd.DataFrame): The 311 cases dataset
            required_columns (list[str]): List of required columns in the DataFrame

        Raises:
            KeyError: If the DataFrame is missing any of the required columns.
        """

        # TODO: Don't forget to add the required_columns parameter with the default value
        self.df = df

    def sort_by_days_open(self,  ascending: bool = False) -> pd.DataFrame:
        """
        Return dataset of 311 cases sorted by how long they were open.
        
        Args:
            ascending (bool): If True, sort from shortest to longest duration
            days_open_column (str): The column name for days open. Default: "days_open"
            
        Returns:
            pd.DataFrame: Sorted dataset
        """
        # TODO: Don't forget to add the days_open_column parameter with the default value
        pass

    def create_urgency_ranking(self) -> dict[str, int]:
        """
        Determine appropriate urgency rankings for each 311 case category.
            
        Returns:
            dict[str, int]: Dictionary mapping categories to urgency scores 
                           (lower = less urgent, higher = more urgent)
        """
        # TODO: you get to decide the "right" ranking for each category.
        # For example, you may decide that "Street and Sidewalk Cleaning"
        # deserves a rank of 300 because it is extremely urgent.
        # You must rank at least 10 different categories found in the dataset.
        pass

    def sort_by_urgency(self, urgency_ranking: dict[str, int]) -> pd.DataFrame:
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
        # TODO: Don't forget to add the category_column parameter with the default value
        pass
