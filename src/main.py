"""
Main program to run the analysis and visualization of 311 cases.
"""

import sys
import pandas as pd
sys.path.append('.')
from src.analysis import Analyzer
from src.sorting import CaseSorter
from src.visualization import Visualizer

DATA_FILE = 'data/311_Cases_SF.csv'

def main() -> None:
    """
    Main function to run analysis and visualization.
    """
     
    # Load the 311 cases dataset
    df = pd.read_csv(DATA_FILE)

    # Sort the data
    sorter = CaseSorter(df)
    sorted_cases = sorter.sort_by_days_open()
    urgency_ranking = sorter.create_urgency_ranking()

    print(f"Sorted Cases by Days Open:\n{sorted_cases.head()}")
    print(f"Urgency Ranking: {urgency_ranking}")

    # Analyze the data
    analyzer = Analyzer(df)
    cases_per_neighborhood = analyzer.cases_per_neighborhood()
    average_days_open = analyzer.average_days_open()
    cases_above_average = analyzer.cases_above_average_per_neighborhood()
    percentage_above_average = analyzer.percentage_above_average_per_neighborhood()

    print(f"Cases per Neighborhood: {cases_per_neighborhood}")
    print(f"Average Days Open: {average_days_open}")
    print(f"Cases Above Average per Neighborhood: {cases_above_average}")
    print(f"Percentage Above Average per Neighborhood: {percentage_above_average}")

    # Visualize the data
    visualizer = Visualizer(df)
    visualizer.plot_percentage_above_average_per_neighborhood()
    visualizer.plot_cases_by_location()

if __name__ == "__main__":
    main()