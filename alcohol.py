import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define model parameters for Republika Srpska
baseline_consumption_rs = 2000000  # Baseline alcohol consumption in liters
current_excise_tax_rs = 2.0  # Current excise tax per liter in BAM
price_elasticity_rs = -0.5  # Price elasticity of demand for alcohol
tax_increase_percentage_rs = 0.2  # 20% increase in excise tax

# Define model parameters for Federation of Bosnia and Herzegovina
baseline_consumption_fbih = 2500000  # Baseline alcohol consumption in liters
current_excise_tax_fbih = 2.0  # Current excise tax per liter in BAM
price_elasticity_fbih = -0.5  # Price elasticity of demand for alcohol
tax_increase_percentage_fbih = 0.2  # 20% increase in excise tax

# Define projection years
years = np.arange(2024, 2031)

# Initialize lists to store results
results_rs = []
results_fbih = []

# Function to calculate new consumption and tax revenue
def calculate_revenue(baseline_consumption, current_excise_tax, price_elasticity, tax_increase_percentage):
    new_excise_tax = current_excise_tax * (1 + tax_increase_percentage)
    price_change_percentage = (new_excise_tax - current_excise_tax) / current_excise_tax
    change_in_consumption_percentage = price_elasticity * price_change_percentage
    new_consumption = baseline_consumption * (1 + change_in_consumption_percentage)
    new_tax_revenue = new_consumption * new_excise_tax
    current_tax_revenue = baseline_consumption * current_excise_tax
    increase_in_tax_revenue = new_tax_revenue - current_tax_revenue
    return new_consumption, new_tax_revenue, increase_in_tax_revenue

# Calculate projections for Republika Srpska
for year in years:
    new_consumption, new_tax_revenue, increase_in_tax_revenue = calculate_revenue(
        baseline_consumption_rs, current_excise_tax_rs, price_elasticity_rs, tax_increase_percentage_rs)
    results_rs.append({'Year': year, 'New_Consumption': new_consumption,
                       'New_Tax_Revenue': new_tax_revenue, 'Increase_in_Tax_Revenue': increase_in_tax_revenue})

# Calculate projections for Federation of Bosnia and Herzegovina
for year in years:
    new_consumption, new_tax_revenue, increase_in_tax_revenue = calculate_revenue(
        baseline_consumption_fbih, current_excise_tax_fbih, price_elasticity_fbih, tax_increase_percentage_fbih)
    results_fbih.append({'Year': year, 'New_Consumption': new_consumption,
                         'New_Tax_Revenue': new_tax_revenue, 'Increase_in_Tax_Revenue': increase_in_tax_revenue})

# Convert results to DataFrames
results_rs_df = pd.DataFrame(results_rs)
results_fbih_df = pd.DataFrame(results_fbih)

# Plotting the projections
sns.set(style="whitegrid")

# Plot for Republika Srpska
plt.figure(figsize=(14, 7))
plt.subplot(1, 2, 1)
plt.plot(results_rs_df['Year'], results_rs_df['New_Consumption'], marker='o', label='New Consumption')
plt.plot(results_rs_df['Year'], results_rs_df['New_Tax_Revenue'], marker='o', label='New Tax Revenue')
plt.plot(results_rs_df['Year'], results_rs_df['Increase_in_Tax_Revenue'], marker='o', label='Increase in Tax Revenue')
plt.title('Projections for Republika Srpska')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend()

# Plot for Federation of Bosnia and Herzegovina
plt.subplot(1, 2, 2)
plt.plot(results_fbih_df['Year'], results_fbih_df['New_Consumption'], marker='o', label='New Consumption')
plt.plot(results_fbih_df['Year'], results_fbih_df['New_Tax_Revenue'], marker='o', label='New Tax Revenue')
plt.plot(results_fbih_df['Year'], results_fbih_df['Increase_in_Tax_Revenue'], marker='o', label='Increase in Tax Revenue')
plt.title('Projections for Federation of Bosnia and Herzegovina')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend()

plt.tight_layout()
plt.show()
