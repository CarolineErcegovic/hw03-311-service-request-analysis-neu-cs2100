"""
Module responsible for visualizing dataset of 311 cases.
"""

import pandas as pd
import matplotlib.pyplot as plt
from src.analysis import Analyzer

REQUIRED_COLUMNS = [
    'CaseID', 'Status', 'Category', 'Street', 'Supervisor District',
    'Neighborhood', 'Police District', 'Latitude', 'Longitude', 'Point',
    'point_geom', 'OpenedDate', 'ClosedDate', 'days_open', 'selected'
]

class Visualizer:
    """
    Class for visualizing 311 cases.
    """

    def __init__(self, df: pd.DataFrame,required_columns: list[str] = REQUIRED_COLUMNS) -> None:
        """
        Initialize with the 311 cases dataset.

        Args:
            df (pd.DataFrame): The 311 cases dataset
            required_columns (list[str]): List of required columns in the DataFrame

        Raises:
            KeyError: If the DataFrame is missing any of the required columns.
        """
        for col in required_columns:
            if col not in df.columns:
                raise KeyError("Not all of the required columns are in the data frame.")

        self.df = df


    def plot_percentage_above_average_per_neighborhood(self,
        neighborhood_column: str = "Neighborhood",
        days_open_column: str = "days_open") -> None:
        """
        Display a bar graph that shows, for each neighborhood, the percentage of cases that stay 
        open longer than the overall average case.

        Args:
            neighborhood_column (str): The column name for neighborhoods. Default: "Neighborhood".
        """
        analyzer = Analyzer(self.df)

        percentages = analyzer.percentage_above_average_per_neighborhood(
            neighborhood_column,
            days_open_column
        )

        neighborhoods = list(percentages.keys())
        values = list(percentages.values())

        plt.figure()
        plt.bar(neighborhoods, values)

        plt.xlabel("Neighborhood")
        plt.ylabel("Percentage of Cases Above Average Days Open")
        plt.title(
            "Percentage of 311 Cases Open Longer Than Average per Neighborhood"
        )

        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()
        

    def plot_cases_by_location(self, latitude_column: str = "Latitude",
        longitude_column: str = "Longitude") -> None:
        """
        Display a scatterplot of cases, with longitude on the horizontal axis and latitude on 
        the vertical axis.

        Args:
            latitude_column (str): The column name for latitude. Default: "Latitude".
            longitude_column (str): The column name for longitude. Default: "Longitude".
        """
        plt.figure()
        plt.scatter(
            self.df[longitude_column],
            self.df[latitude_column]
        )

        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.title("311 Cases by Geographic Location")

        plt.tight_layout()
        plt.show()
