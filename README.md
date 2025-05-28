# Alcohol Excise Tax Revenue Projections (Bosnia and Herzegovina)

This repository contains a Python simulation model that estimates the impact of a 20% increase in alcohol excise taxes in Bosnia and Herzegovina’s two entities: Republika Srpska and the Federation of Bosnia and Herzegovina.

## Objective

To project changes in:
- Alcohol consumption
- Excise tax revenue
- Net increase in government revenue

...over the period 2024–2030, using basic economic modeling with price elasticity of demand.

## Key Parameters

| Region                  | Baseline Consumption | Current Excise Tax | Price Elasticity | Tax Increase |
|-------------------------|----------------------|---------------------|------------------|--------------|
| Republika Srpska        | 2,000,000 liters     | 2.00 BAM/L          | -0.5             | +20%         |
| Federation of BiH       | 2,500,000 liters     | 2.00 BAM/L          | -0.5             | +20%         |

## Model Approach

1. Apply a 20% excise tax increase.
2. Estimate consumption change using price elasticity of demand.
3. Calculate new tax revenue and compare it to baseline.

## Visualization

Two side-by-side line plots show projections for:
- New consumption (in liters)
- New tax revenue (in BAM)
- Net increase in tax revenue (in BAM)

## How to Run

1. Install dependencies:
    ```bash
    pip install pandas matplotlib seaborn
    ```

2. Run the script:
    ```bash
    python alcohol_tax_projection.py
    ```
