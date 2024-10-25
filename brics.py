import pandas as pd

# Define BRICS countries (including new members as of 2024)
# Hey, who knew BRICS would become such a big club?

brics_countries = [
    "Brazil",
    "Russia",
    "India",
    "China",
    "South Africa",
    "Ethiopia",
    "United Arab Emirates",
    "Iran",
    "Saudi Arabia",
    "Egypt",
]


# data:

governance_index = [
    -0.29333333333333333,
    -1.0333333333333334,
    -0.06833333333333333,
    -0.33166666666666667,
    -0.105,
    -0.975,
    +0.65,
    -1.2783333333333333,
    -0.03333333333333335,
    -0.7633333333333333,
]

inflation_Rate = [4.42, 8.6, 5.49, 0.4, 3.8, 17.5, 2.5, 31.2, 1.7, 26.4]
# source: trading economic

unemployment_rates = [7.95, 2.4, 7.8, 5.1, 33.5, 18.9, 2.95, 7.5, 3.3, 6.5]
# source: trading economic
gdp_growth_rates = [1.4, 3.6, 1.3, 0.9, 0.4, 7.9, 3.4, 4.6, 1.4, 2.4]
# source: trading economic

public_debt = [74.42, 14.9, 81.59, 83.6, 72.2, 38, 29.9, 30.6, 30, 95.8]
# source: trading economic

political_stability = [34, 16, 25, 28, 20, 5, 70, 8, 32, 14]
# source: data world bank

military_conflicts = [1, 1, 1, 1, 0, 1, 0, 1, 1, 1]
# source: ourworldindata.org

democracy_index = [6.7, 2.2, 7.2, 2.1, 7, 3.4, 3, 2, 2.1, 2.9]
# source: ourworldindata.org

corruption_scores = [36, 26, 39, 42, 41, 37, 68, 24, 52, 35]
# source: transparency.org

government_effectiveness = [
    -0.59,
    -0.70,
    0.37,
    0.50,
    -0.13,
    -0.75,
    1.30,
    -0.88,
    0.58,
    -0.45,
]
# source: theglobaleconomy.com


# Create a DataFrame
data = {
    "Country": brics_countries,
    "inflation_Rate": inflation_Rate,
    "Unemployment_Rate": unemployment_rates,
    "GDP_Growth_Rate": gdp_growth_rates,
    "Public_Debt": public_debt,
    "Political_Stability_Index": political_stability,
    "Military_Conflicts": military_conflicts,
    "Democracy_Index": democracy_index,
    "Governance_Index": governance_index,
    "Corruption_Score": corruption_scores,  # Updated to use scores
    "Government_Effectiveness": government_effectiveness,  # Updated to use Government Effectiveness
}

df = pd.DataFrame(data)


# P(Failure) = Σ (Wi × Pi)
class BRICSAnalyzer:
    """
    A class to analyze the probability of BRICS alliance failure based on various economic
    and political indicators.

    Think of this as a crystal ball for international politics, but with more math! 
    """

    def __init__(self, data_df):
        """
        Initialize the analyzer with a pandas DataFrame containing country data.

        Parameters:
        -----------
        data_df : pandas DataFrame
            Must include columns for economic and political indicators
        """
        self.data = data_df

        # Define risk weights for different factors
        # Just like cooking, it's all about the right proportions! 
        self.weights = {
            "Economic_Stability": 0.30,  # Because money talks!
            "Geopolitical_Tensions": 0.25,  # Can't we all just get along?
            "Global_Economic_Environment": 0.20,  # The world is watching
            "Implementation_and_Governance": 0.25,  # Rules of the game
        }

    def calculate_economic_risk(self):
        """Calculate economic risk based on inflation, unemployment, and debt."""
        return (
            self.data["inflation_Rate"].mean() / 100 * 0.4
            + self.data["Unemployment_Rate"].mean() / 100 * 0.3
            + self.data["Public_Debt"].mean() / 100 * 0.3
        )

    def calculate_political_risk(self):
        """Calculate political risk based on stability and democracy indices."""
        return (100 - self.data["Political_Stability_Index"].mean()) / 100 * 0.5 + (
            10 - self.data["Democracy_Index"].mean()
        ) / 10 * 0.5

    def calculate_governance_risk(self):
        """Calculate governance risk based on corruption and effectiveness."""
        return (100 - self.data["Corruption_Score"].mean()) / 100 * 0.5 + (
            2 - self.data["Government_Effectiveness"].mean()
        ) / 4 * 0.5

    def calculate_failure_probability(self):
        """
        Calculate the overall probability of BRICS failure.

        Returns:
        --------
        float : Probability of failure as a percentage
        """
        # Calculate individual risk factors
        economic_risk = self.calculate_economic_risk()
        political_risk = self.calculate_political_risk()
        governance_risk = self.calculate_governance_risk()

        # Calculate weighted average of risks
        overall_probability = (
            self.weights["Economic_Stability"] * economic_risk
            + self.weights["Geopolitical_Tensions"] * political_risk
            + self.weights["Global_Economic_Environment"] * 0.5  # Base global risk
            + self.weights["Implementation_and_Governance"] * governance_risk
        )

        return overall_probability * 100

    def generate_summary(self):
        """Generate a summary of key metrics and the final probability."""
        summary = {
            "Average_Inflation": int(self.data["inflation_Rate"].mean()),
            "Average_Unemployment": int(self.data["Unemployment_Rate"].mean()),
            "Average_Democracy_Index": int(self.data["Democracy_Index"].mean()),
            "Average_Corruption_Score": int(self.data["Corruption_Score"].mean()),
            "Failure_Probability": int(self.calculate_failure_probability()),
        }
        return summary


# see result
sm = BRICSAnalyzer(df).generate_summary()
print(sm)
