"""
Module responsible for analyzing dataset of 311 cases.
"""
import pandas as pd
REQUIRED_COLUMNS = [
    'CaseID', 'Status', 'Category', 'Street', 'Supervisor District',
    'Neighborhood', 'Police District', 'Latitude', 'Longitude', 'Point',
    'point_geom', 'OpenedDate', 'ClosedDate', 'days_open', 'selected'
]

class Analyzer:
    """
    Class for analyzing 311 cases.
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
            
    def cases_per_neighborhood(self, neighborhood_column: str = "Neighborhood") -> dict[str, int]:
        """
        Count the total number of cases per neighborhood.

        Args:
            neighborhood_column (str): The column name for neighborhoods. Default: "Neighborhood".

        Returns:
            dict[str, int]: A dictionary with neighborhoods as keys and case counts as values.
        """
        counts = self.df[neighborhood_column].value_counts()
        return {str(k): int(v) for k, v in counts.items()}

    def average_days_open(self, days_open_column: str = "days_open") -> float:
        """
        Calculate the average number of days that a case stays open.

        Args:
            days_open_column (str): The column name for days open. Default: "days_open".

        Returns:
            float: The average number of days that cases stay open.
        """
        return float(self.df[days_open_column].mean())


    def cases_above_average_per_neighborhood(self,  neighborhood_column: str = "Neighborhood",
        days_open_column: str = "days_open") -> dict[str, int]:
        """
        Count the number of cases that stay open longer than average, for each neighborhood.

        Args:
            neighborhood_column (str): The column name for neighborhoods. Default: "Neighborhood".
            days_open_column (str): The column name for days open. Default: "days_open".

        Returns:
            dict[str, int]: A dictionary with neighborhoods as keys and counts of cases 
                above average as values.
        """
        average = self.average_days_open(days_open_column)

        df_copy = self.df.copy()
        df_copy["above_average"] = df_copy[days_open_column] > average

        counts = df_copy.groupby(neighborhood_column)["above_average"].sum()

        return {str(k): int(v) for k, v in counts.items()}

    def percentage_above_average_per_neighborhood(self,neighborhood_column: str = "Neighborhood",
        days_open_column: str = "days_open") -> dict[str, float]:
        """
        Calculate the percentage of cases that stay open longer than average, for each neighborhood.

        Args:
            neighborhood_column (str): The column name for neighborhoods. Default: "Neighborhood".
            days_open_column (str): The column name for days open. Default: "days_open".

        Returns:
            dict[str, float]: A dictionary with neighborhoods as keys and percentages as values.
        """
        total_counts = self.cases_per_neighborhood(neighborhood_column)
        above_counts = self.cases_above_average_per_neighborhood(
            neighborhood_column,
            days_open_column
        )

        percentages = {}

        for neighborhood in total_counts:
            total = total_counts[neighborhood]
            above = above_counts.get(neighborhood, 0)

            percentages[neighborhood] = (above / total) * 100 if total > 0 else 0.0

        return percentages
