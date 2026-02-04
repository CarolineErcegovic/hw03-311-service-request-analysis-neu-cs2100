"""
Module responsible for visualizing dataset of 311 cases.
"""

import pandas as pd
import matplotlib.pyplot as plt

class Visualizer:
    """
    Class for visualizing 311 cases.
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
        # TODO: Don't forget to add the required_columns parameter with default value
        self.df = df


    def plot_percentage_above_average_per_neighborhood(self) -> None:
        """
        Display a bar graph that shows, for each neighborhood, the percentage of cases that stay 
        open longer than the overall average case.

        Args:
            neighborhood_column (str): The column name for neighborhoods. Default: "Neighborhood".
        """
        # TODO: Make sure to include a label for the x-axis, the y-axis, and the overall graph
        # TODO: Make sure to label the "ticks" on the x-axis so we know which neighborhood is which
        pass

    def plot_cases_by_location(self) -> None:
        """
        Display a scatterplot of cases, with longitude on the horizontal axis and latitude on 
        the vertical axis.

        Args:
            latitude_column (str): The column name for latitude. Default: "Latitude".
            longitude_column (str): The column name for longitude. Default: "Longitude".
        """
        # TODO: Don't forget to add the latitude_column and longitude_column parameters 
        # with default values
        # TODO: Make sure to include a label for the x-axis, the y-axis, and the overall graph
        pass
