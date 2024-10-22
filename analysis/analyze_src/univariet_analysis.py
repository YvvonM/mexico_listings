#importing libraries
from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import random

# Abstract Base Class for Univariate Analysis Strategy
# -----------------------------------------------------
# This class defines a common interface for univariate analysis strategies.
# Subclasses must implement the analyze method.
class UnivarietAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature: str):
         """
        Perform univariate analysis on a specific feature of the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature (str): The name of the feature/column to be analyzed.

        Returns:
        None: This method visualizes the distribution of the feature.
        """
         pass

class NumericalUnivarietAnalysis(UnivarietAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature: str):
        """
        Plots the distribution of a numerical feature using a histogram and KDE.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature (str): The name of the numerical feature/column to be analyzed.

        Returns:
        None: Displays a histogram with a KDE plot.
        """
        colors = ['blue', 'green', 'red', 'purple', 'orange', 
       'pink', 'yellow', 'cyan', 'magenta', 'brown', 
       'gray', 'lime', 'navy', 'teal', 'maroon', 
       'olive', 'violet', 'gold', 'silver', 'indigo']
        color = random.choice(colors)
        plt.figure(figsize=(7, 5))
        sns.histplot(df[feature], kde= True, color= color)
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()
# Concrete Strategy for Categorical Features
# -------------------------------------------
# This strategy analyzes categorical features by plotting their frequency distribution.
class CategoricalUnivarietAnalysis(UnivarietAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature: str):
        """
        Plots the distribution of a categorical feature using a bar plot.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature (str): The name of the categorical feature/column to be analyzed.

        Returns:
        None: Displays a bar plot.
        """
        
        plt.figure(figsize=(7, 5))
        sns.countplot(data = df,x = feature, palette= 'muted')
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.xticks(rotation = 70)
        plt.show()

# Context Class that uses a UnivariatAnalysisStrategy
# ----------------------------------------------------
# This class allows you to switch between different univariate analysis strategies.
class UnivarietAnalyzer:
    def __init__(self, strategy: UnivarietAnalysisStrategy):
         """
        Initializes the UnivariateAnalyzer with a specific analysis strategy.

        Parameters:
        strategy (UnivariateAnalysisStrategy): The strategy to be used for univariate analysis.

        Returns:
        None
        """
         self._strategy = strategy

    def set_strategy(self, strategy: UnivarietAnalysisStrategy):
        """
        Sets a new strategy for the UnivarietAnalyzer.

        Parameters:
        strategy (UnivarietAnalysisStrategy): The new strategy to be used for data visualization.

        Returns:
        None
        """
        self._strategy = strategy

    def execute_analysis(self, df: pd.DataFrame, feature: str):
        """
        Executes the univariate analysis using the current strategy.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data.
        feature (str): The name of the feature/column to be analyzed.

        Returns:
        None: Executes the strategy's analysis method and visualizes the results.
        """
        self._strategy.analyze(df, feature)

if __name__ == '__main__':
    pass