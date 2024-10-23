# importing libraries
from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Abstract Base Class for Bivariate Analysis Strategy
# ----------------------------------------------------
# This class defines a common interface for bivariate analysis strategies.
# Subclasses must implement the analyze method.
class BivarietAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
         """
        Perform bivariate analysis on two features of the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature1 (str): The name of the first feature/column to be analyzed.
        feature2 (str): The name of the second feature/column to be analyzed.

        Returns:
        None: This method visualizes the relationship between the two features.
        """
         pass


# Concrete Strategy for Numerical vs Numerical Analysis
# ------------------------------------------------------
# This strategy analyzes the relationship between two numerical features using scatter plots.
class NumericalVsNumericalAnalysis(BivarietAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        Perform bivariate analysis on two numerical features of the dataframe using scatter plots.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature1 (str): The name of the first feature/column to be analyzed.
        feature2 (str): The name of the second feature/column to be analyzed.

        Returns:
        None: This method visualizes the relationship between the two numerical features.
        """
        colors = ['blue', 'green', 'red', 'purple', 'orange', 
       'pink', 'yellow', 'cyan', 'magenta', 'brown', 
       'gray', 'lime', 'navy', 'teal', 'maroon', 
       'olive', 'violet', 'gold', 'silver', 'indigo']
        color = random.choice(colors)
        plt.figure(figsize= (7,5))
        sns.scatterplot(data = df, x = feature1, y = feature2, color = color)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()

# Concrete Strategy for Numerical vs Categorical Analysis
# ------------------------------------------------------
# This strategy analyzes the relationship between a numerical feature and a categorical feature using box plots.
class NumericalVsCategoricalAnalysis(BivarietAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        Perform bivariate analysis between numeric and categorical columns of the dataframe using scatter plots.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature1 (str): The name of the first feature/column to be analyzed.
        feature2 (str): The name of the second feature/column to be analyzed.

        Returns:
        None: This method visualizes the relationship between the numeric and categorical features.
        """
        colors = ['blue', 'green', 'red', 'purple', 'orange', 
       'pink', 'yellow', 'cyan', 'magenta', 'brown', 
       'gray', 'lime', 'navy', 'teal', 'maroon', 
       'olive', 'violet', 'gold', 'silver', 'indigo']
        color = random.choice(colors)
        plt.figure(figsize= (7,5))
        sns.boxplot(data = df, x = feature1, y = feature2, color = color)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.xticks(rotation = 45)
        plt.show()

# Context Class that uses a BivariateAnalysisStrategy
# ---------------------------------------------------
# This class allows you to switch between different bivariate analysis strategies.
class BivarietAnalyzer:
    def __init__(self, strategy: BivarietAnalysisStrategy):
        """
        Initializes the BivariateAnalyzer with a specific analysis strategy.

        Parameters:
        strategy (BivariateAnalysisStrategy): The strategy to be used for bivariate analysis.

        Returns:
        None
        """
        self._strategy = strategy

    def set_strategy(self, strategy: BivarietAnalysisStrategy):
        """
        Sets a new strategy for the BivariateAnalyzer.

        Parameters:
        strategy (BivariateAnalysisStrategy): The new strategy to be used for bivariate analysis.

        Returns:
        None
        """
        self._strategy = strategy

    def execute_analysis(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        Executes the bivariate analysis using the current strategy.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature1 (str): The name of the first feature/column to be analyzed.
        feature2 (str): The name of the second feature/column to be analyzed.

        Returns:
        None: Executes the strategy's analysis method and visualizes the results.
        """
        self._strategy.analyze(df, feature1, feature2)

if __name__ == '__main__':
    pass