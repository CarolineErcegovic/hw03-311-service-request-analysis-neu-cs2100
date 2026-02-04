"""
Module responsible for analyzing dataset of 311 cases.
"""

import pandas as pd

class Analyzer:
    """
    Class for analyzing 311 cases.
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

    def cases_per_neighborhood(self) -> dict[str, int]:
        """
        Count the total number of cases per neighborhood.

        Args:
            neighborhood_column (str): The column name for neighborhoods. Default: "Neighborhood".

        Returns:
            dict[str, int]: A dictionary with neighborhoods as keys and case counts as values.
        """
        # TODO: Don't forget to add the neighborhood_column parameter with the default value
        pass

    def average_days_open(self) -> float:
        """
        Calculate the average number of days that a case stays open.

        Args:
            days_open_column (str): The column name for days open. Default: "days_open".

        Returns:
            float: The average number of days that cases stay open.
        """
        # TODO: Don't forget to add the days_open_column parameter with the default value
        pass

    def cases_above_average_per_neighborhood(self) -> dict[str, int]:
        """
        Count the number of cases that stay open longer than average, for each neighborhood.

        Args:
            neighborhood_column (str): The column name for neighborhoods. Default: "Neighborhood".
            days_open_column (str): The column name for days open. Default: "days_open".

        Returns:
            dict[str, int]: A dictionary with neighborhoods as keys and counts of cases 
                above average as values.
        """
        # TODO: Don't forget to add the neighborhood_column and days_open_column parameters
        # with the default values
        pass

    def percentage_above_average_per_neighborhood(self) -> dict[str, float]:
        """
        Calculate the percentage of cases that stay open longer than average, for each neighborhood.

        Args:
            neighborhood_column (str): The column name for neighborhoods. Default: "Neighborhood".
            days_open_column (str): The column name for days open. Default: "days_open".

        Returns:
            dict[str, float]: A dictionary with neighborhoods as keys and percentages as values.
        """
        # TODO: Don't forget to add the neighborhood_column and days_open_column parameters
        # with the default values
        pass
