# 🐓 Rooster AI Forecasting Platform

An end-to-end demand forecasting system for poultry demand planning built using Python, CatBoost, and Streamlit.

The platform helps sales teams estimate future demand, compare recommendations against historical performance, and make more informed ordering decisions.

---

# Business Problem

In many poultry businesses, ordering decisions depend heavily on experience and intuition.

This often leads to:

- Excess inventory and unnecessary waste
- Product shortages and missed sales opportunities

The objective of this project was to build a forecasting solution that transforms historical sales data into actionable demand recommendations.

---

# Forecasting Drivers

The model incorporates multiple demand drivers:

| Driver | Business Impact |
|----------|----------|
| Seasonality | Historical demand patterns |
| Weekends | Thursday / Friday effect |
| Public Holidays | Demand fluctuations during holidays |
| Ramadan | Seasonal demand changes |
| Eid Al-Fitr | Demand spikes |
| Eid Al-Adha | Demand spikes |
| Promotions | Promotion influence on sales |
| Slaughterhouse Availability | Supply-side constraints |
| Lag Features | Recent demand memory |
| Rolling Features | Trend smoothing |

---

# Feature Engineering

## Date Features

- Day Of Week
- Day Of Month
- Month
- Week Of Year
- Quarter
- Is Month Start
- Is Month End

## Lag Features

- Lag 1
- Lag 7
- Lag 14
- Lag 30

## Rolling Features

- Rolling Mean 7
- Rolling Mean 14
- Rolling Mean 30

---

# Machine Learning Model

## Model

**CatBoost Regressor**

## Why CatBoost?

- Native support for categorical variables
- Strong performance on tabular business datasets
- Minimal preprocessing requirements
- Excellent handling of mixed feature types

## Forecast Horizon

The system generates recursive **7-day forecasts** where each prediction contributes to future lag calculations.

---

# Dashboard Features

Built using Streamlit.

## Interactive Filtering

- Channel
- Pricing Group
- Product

## KPI Cards

- AI Suggested Demand
- Last Month Actual
- Growth %

## Analytics

- Forecast vs Actual Comparison
- Daily Forecast Plan
- Forecast Download
- Interactive Visualization

## Authentication

- Demo Login System
- Company-style user experience

---

# Dataset

The dataset included in this repository has been fully anonymized.

Examples:

| Original Data | Portfolio Version |
|---------------|-------------------|
| Product Name | SKU-001 |
| Customer Name | Customer-001 |
| Sales Channel | Channel-001 |

The anonymization preserves business behavior while protecting sensitive company information.

---

# Project Structure

```text
Rooster-AI-Forecasting-Platform

├── portapp.py
├── Portfolio.py
├── Rooster_Dataset.xlsx
├── Forecast_Output.xlsx
├── Actual_Last_Month_Output.xlsx
├── BG3.png
├── Plogo.png
├── requirements.txt
└── README.md
```

---

# Tech Stack

- Python
- Pandas
- NumPy
- CatBoost
- Plotly
- Streamlit
- OpenPyXL

---

# Run Locally

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Generate Forecasts

```bash
python Portfolio.py
```

## Launch Dashboard

```bash
streamlit run portapp.py
```

---

# Demo Credentials

### Email

```text
demo@rooster.net
```

### Password

```text
1111
```

---

# Key Takeaway

Building the forecasting model was only part of the challenge.

A significant portion of the work involved:

- Business understanding
- Data collection
- Feature engineering
- Demand driver identification
- Dashboard development
- Forecast interpretation

The final result is a business-oriented demand forecasting platform designed to support operational decision-making.

---

# Author

**Abdelrahman Melouk**

- GitHub: https://github.com/AbdelrahmanMelouk
- LinkedIn: https://www.linkedin.com/in/abdelrahman-melouk