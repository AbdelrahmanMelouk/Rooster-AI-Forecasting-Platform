import pandas as pd
import numpy as np

# =====================================
# File Paths
# =====================================

historical_path = r"C:\Users\abdur\Desktop\Forcast Fresh Marinate\Product\Historical Data.xlsx"

promotion_path = r"C:\Users\abdur\Desktop\Forcast Fresh Marinate\Product\promotion.xlsx"

calendar_path = r"C:\Users\abdur\Desktop\Forcast Fresh Marinate\Product\Calender.xlsx"

# =====================================
# Load Files
# =====================================

historical = pd.read_excel(historical_path)

promotion = pd.read_excel(promotion_path)

calendar = pd.read_excel(calendar_path)

# =====================================
# Clean Columns
# =====================================

historical.columns = (
    historical.columns
    .str.strip()
    .str.replace(" ", "_")
)

promotion.columns = (
    promotion.columns
    .str.strip()
    .str.replace(" ", "_")
)

calendar.columns = (
    calendar.columns
    .str.strip()
    .str.replace(" ", "_")
)

# =====================================
# Check Columns
# =====================================

print("\nHistorical Columns:")
print(historical.columns.tolist())

print("\nPromotion Columns:")
print(promotion.columns.tolist())

print("\nCalendar Columns:")
print(calendar.columns.tolist())

# =====================================
# Date Format
# =====================================

historical["Date"] = pd.to_datetime(
    historical["Date"]
)

promotion["Date"] = pd.to_datetime(
    promotion["Date"]
)

calendar["Date"] = pd.to_datetime(
    calendar["Date"]
)

# =====================================
# Select Historical Columns
# =====================================

historical = historical[
    [
        "Date",
        "Sub_Channels",
        "Pricing_Group",
        "Name",
        "Quantity",
        "Required_Qty"
    ]
]

# =====================================
# Select Promotion Columns
# =====================================

promotion = promotion[
    [
        "Date",
        "Sub_Channels",
        "Pricing_Group",
        "Name",
        "Is_Promted",
        "Available_Promoted"
    ]
]

# =====================================
# Select Calendar Columns
# =====================================

calendar = calendar[
    [
        "Date",
        "Is_Holiday",
        "Is_Ramadan",
        "Is_Eid_Fitr",
        "Is_Eid_Adha",
        "Is_SLH_Holiday",
        "SLH_Availability",
        "Day_Name"
    ]
]

# =====================================
# Merge Promotion
# =====================================

merged_df = historical.merge(
    promotion,
    how="left",
    on=[
        "Date",
        "Sub_Channels",
        "Pricing_Group",
        "Name"
    ]
)

# =====================================
# Merge Calendar
# =====================================

merged_df = merged_df.merge(
    calendar,
    how="left",
    on="Date"
)

# =====================================
# Fill Promotion Missing
# =====================================

merged_df["Is_Promted"] = (
    merged_df["Is_Promted"]
    .fillna(0)
)

merged_df["Available_Promoted"] = (
    merged_df["Available_Promoted"]
    .fillna(0)
)

# =====================================
# Fill Calendar Missing
# =====================================

calendar_cols = [
    "Is_Holiday",
    "Is_Ramadan",
    "Is_Eid_Fitr",
    "Is_Eid_Adha",
    "Is_SLH_Holiday",
    "SLH_Availability"
]

for col in calendar_cols:

    merged_df[col] = (
        merged_df[col]
        .fillna(0)
    )

# =====================================
# Clean Target
# =====================================

merged_df["Required_Qty"] = (
    merged_df["Required_Qty"]
    .fillna(0)
)

# =====================================
# Validation
# =====================================

print("\n====================")
print("Shape")
print("====================")

print(merged_df.shape)

print("\n====================")
print("Columns")
print("====================")

print(merged_df.columns.tolist())

print("\n====================")
print("Missing Values")
print("====================")

print(
    merged_df.isnull()
    .sum()
)

print("\n====================")
print("Promotion Check")
print("====================")

print(
    merged_df[
        [
            "Is_Promted",
            "Available_Promoted"
        ]
    ]
    .value_counts()
    .head(20)
)

print("\n====================")
print("Holiday Check")
print("====================")

print(
    merged_df[
        [
            "Is_Holiday",
            "Is_Ramadan",
            "Is_Eid_Fitr",
            "Is_Eid_Adha",
            "Is_SLH_Holiday"
        ]
    ]
    .sum()
)

print("\n====================")
print("Sample Data")
print("====================")

print(
    merged_df.head(20)
)

# =====================================
# Aggregate Data
# =====================================

product_sales = (
    merged_df
    .groupby(
        [
            "Date",
            "Name",
            "Sub_Channels",
            "Pricing_Group"
        ]
    )
    .agg({

        "Required_Qty": "sum",

        "Is_Promted": "max",
        "Available_Promoted": "max",

        "Is_Holiday": "max",
        "Is_Ramadan": "max",
        "Is_Eid_Fitr": "max",
        "Is_Eid_Adha": "max",

        "Is_SLH_Holiday": "max",
        "SLH_Availability": "max"

    })
    .reset_index()
)

product_sales["Required_Qty"] = (
    product_sales["Required_Qty"]
    .clip(lower=0)
)

# =====================================
# Portfolio Anonymization
# =====================================

# Products
product_map = {
    value: f"SKU-{i+1:03d}"
    for i, value in enumerate(
        sorted(product_sales["Name"].unique())
    )
}

# Customers
customer_map = {
    value: f"Customer-{i+1:03d}"
    for i, value in enumerate(
        sorted(product_sales["Pricing_Group"].unique())
    )
}

# Channels
channel_map = {
    value: f"Channel-{i+1:03d}"
    for i, value in enumerate(
        sorted(product_sales["Sub_Channels"].unique())
    )
}

product_sales["Name"] = (
    product_sales["Name"]
    .map(product_map)
)

product_sales["Pricing_Group"] = (
    product_sales["Pricing_Group"]
    .map(customer_map)
)

product_sales["Sub_Channels"] = (
    product_sales["Sub_Channels"]
    .map(channel_map)
)

# =====================================
# Check Shape
# =====================================

print("\n====================")
print("After Aggregation")
print("====================")

print(product_sales.shape)

print("\n====================")
print("Sample")
print("====================")

print(
    product_sales.head()
)

# =====================================
# Sort Data
# =====================================

product_sales = product_sales.sort_values(
    [
        "Name",
        "Sub_Channels",
        "Pricing_Group",
        "Date"
    ]
)

# =====================================
# Group Key
# =====================================

group_cols = [
    "Name",
    "Sub_Channels",
    "Pricing_Group"
]

# =====================================
# Date Features
# =====================================

product_sales["dayofweek"] = (
    product_sales["Date"]
    .dt.dayofweek
)

product_sales["day"] = (
    product_sales["Date"]
    .dt.day
)

product_sales["month"] = (
    product_sales["Date"]
    .dt.month
)

product_sales["weekofyear"] = (
    product_sales["Date"]
    .dt
    .isocalendar()
    .week
    .astype(int)
)

product_sales["quarter"] = (
    product_sales["Date"]
    .dt.quarter
)

product_sales["is_month_start"] = (
    product_sales["Date"]
    .dt.is_month_start
).astype(int)

product_sales["is_month_end"] = (
    product_sales["Date"]
    .dt.is_month_end
).astype(int)

print("\n====================")
print("After Date Features")
print("====================")

print(product_sales.shape)

print(
    product_sales.head()
)

# =====================================
# Lag Features
# =====================================

product_sales["lag_1"] = (
    product_sales
    .groupby(group_cols)["Required_Qty"]
    .shift(1)
)

product_sales["lag_7"] = (
    product_sales
    .groupby(group_cols)["Required_Qty"]
    .shift(7)
)

product_sales["lag_14"] = (
    product_sales
    .groupby(group_cols)["Required_Qty"]
    .shift(14)
)

product_sales["lag_30"] = (
    product_sales
    .groupby(group_cols)["Required_Qty"]
    .shift(30)
)

# =====================================
# Rolling Features
# =====================================

product_sales["rolling_7"] = (
    product_sales
    .groupby(group_cols)["Required_Qty"]
    .transform(
        lambda x:
        x.shift(1)
         .rolling(7)
         .mean()
    )
)

product_sales["rolling_14"] = (
    product_sales
    .groupby(group_cols)["Required_Qty"]
    .transform(
        lambda x:
        x.shift(1)
         .rolling(14)
         .mean()
    )
)

product_sales["rolling_30"] = (
    product_sales
    .groupby(group_cols)["Required_Qty"]
    .transform(
        lambda x:
        x.shift(1)
         .rolling(30)
         .mean()
    )
)

# =====================================
# Check Lag Features
# =====================================

print("\n====================")
print("After Lag Features")
print("====================")

print(product_sales.shape)

print(
    product_sales[
        [
            "Name",
            "Date",
            "Required_Qty",
            "lag_1",
            "lag_7",
            "rolling_7"
        ]
    ].head(20)
)

# =====================================
# Remove Nulls
# =====================================

product_sales = product_sales.dropna()

print("\n====================")
print("After Drop NA")
print("====================")

print(product_sales.shape)


features = [

    # Categorical
    "Name",
    "Sub_Channels",
    "Pricing_Group",

    # Lag
    "lag_1",
    "lag_7",
    "lag_14",
    "lag_30",

    # Rolling
    "rolling_7",
    "rolling_14",
    "rolling_30",

    # Date
    "dayofweek",
    "day",
    "month",
    "weekofyear",
    "quarter",

    "is_month_start",
    "is_month_end",

    # Promotion
    "Is_Promted",
    "Available_Promoted",

    # Calendar
    "Is_Holiday",
    "Is_Ramadan",
    "Is_Eid_Fitr",
    "Is_Eid_Adha",

    # Plant
    "Is_SLH_Holiday",
    "SLH_Availability"

]


# =====================================
# Train On All Data
# =====================================
target = "Required_Qty" 
x_train = product_sales[features]

y_train = product_sales[target]

cat_features = [
    "Name",
    "Sub_Channels",
    "Pricing_Group"
]

from catboost import CatBoostRegressor

model = CatBoostRegressor(
    iterations=852,
    learning_rate=0.03,
    depth=8,
    random_seed=42,
    verbose=100
)

model.fit(
    x_train,
    y_train,
    cat_features=cat_features
)

# =====================================
# Feature Importance
# =====================================

importance = pd.DataFrame({
    "Feature": features,
    "Importance":
    model.get_feature_importance()
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n====================")
print("Feature Importance")
print("====================")

print(importance)


# =====================================
# Future 7 Days Forecast
# =====================================

last_date = product_sales["Date"].max()

print("\n====================")
print("Last Historical Date")
print("====================")

print(last_date)

future_dates = pd.date_range(
    start=last_date + pd.Timedelta(days=1),
    periods=7,
    freq="D"
)

forecast_results = []

history = product_sales.copy()

for current_date in future_dates:

    unique_groups = (
        history[
            [
                "Name",
                "Sub_Channels",
                "Pricing_Group"
            ]
        ]
        .drop_duplicates()
    )

    future_rows = []

    for _, row in unique_groups.iterrows():

        name = row["Name"]
        channel = row["Sub_Channels"]
        pricing = row["Pricing_Group"]

        group_history = history[
            (history["Name"] == name)
            &
            (history["Sub_Channels"] == channel)
            &
            (history["Pricing_Group"] == pricing)
        ].sort_values("Date")

        demand_series = (
            group_history["Required_Qty"]
            .tolist()
        )

        if len(demand_series) < 30:
            continue

        lag_1 = demand_series[-1]
        lag_7 = demand_series[-7]
        lag_14 = demand_series[-14]
        lag_30 = demand_series[-30]

        rolling_7 = np.mean(
            demand_series[-7:]
        )

        rolling_14 = np.mean(
            demand_series[-14:]
        )

        rolling_30 = np.mean(
            demand_series[-30:]
        )

        calendar_row = calendar[
            calendar["Date"] == current_date
        ]

        if len(calendar_row) > 0:

            is_holiday = calendar_row[
                "Is_Holiday"
            ].iloc[0]

            is_ramadan = calendar_row[
                "Is_Ramadan"
            ].iloc[0]

            is_eid_fitr = calendar_row[
                "Is_Eid_Fitr"
            ].iloc[0]

            is_eid_adha = calendar_row[
                "Is_Eid_Adha"
            ].iloc[0]

            is_slh_holiday = calendar_row[
                "Is_SLH_Holiday"
            ].iloc[0]

            slh_availability = calendar_row[
                "SLH_Availability"
            ].iloc[0]

        else:

            is_holiday = 0
            is_ramadan = 0
            is_eid_fitr = 0
            is_eid_adha = 0
            is_slh_holiday = 0
            slh_availability = 0

        future_rows.append({

            "Date": current_date,

            "Name": name,

            "Sub_Channels": channel,

            "Pricing_Group": pricing,

            "lag_1": lag_1,
            "lag_7": lag_7,
            "lag_14": lag_14,
            "lag_30": lag_30,

            "rolling_7": rolling_7,
            "rolling_14": rolling_14,
            "rolling_30": rolling_30,

            "dayofweek": current_date.dayofweek,

            "day": current_date.day,

            "month": current_date.month,

            "weekofyear":
            current_date.isocalendar().week,

            "quarter":
            ((current_date.month - 1) // 3) + 1,

            "is_month_start":
            int(
                current_date.is_month_start
            ),

            "is_month_end":
            int(
                current_date.is_month_end
            ),

            "Is_Promted": 0,

            "Available_Promoted": 1,

            "Is_Holiday": is_holiday,

            "Is_Ramadan": is_ramadan,

            "Is_Eid_Fitr": is_eid_fitr,

            "Is_Eid_Adha": is_eid_adha,

            "Is_SLH_Holiday":
            is_slh_holiday,

            "SLH_Availability":
            slh_availability

        })

    future_df = pd.DataFrame(
        future_rows
    )

    if len(future_df) == 0:
        continue

    future_df["prediction"] = (
        model.predict(
            future_df[features]
        )
    )

    future_df["prediction"] = (
        future_df["prediction"]
        .clip(lower=0)
    )

    forecast_results.append(
        future_df
    )

    temp_history = future_df.copy()

    temp_history["Required_Qty"] = (
        temp_history["prediction"]
    )

    history = pd.concat(
        [
            history,
            temp_history
        ],
        ignore_index=True
    )

# =====================================
# Final Forecast
# =====================================
if len(forecast_results) == 0:

    raise ValueError(
        "No Forecast Results Generated"
    )

forecast_df = pd.concat(
    forecast_results,
    ignore_index=True
)

forecast_df = forecast_df.rename(
    columns={
        "Name": "Product",
        "Sub_Channels": "Channel",
        "Pricing_Group": "Pricing Group",
        "prediction": "Predicted"
    }
)

forecast_df = forecast_df[
    [
        "Date",
        "Product",
        "Channel",
        "Pricing Group",
        "Predicted"
    ]
]

forecast_df["Predicted"] = (
    forecast_df["Predicted"]
    .round(0)
    .astype(int)
)

print("\n====================")
print("Forecast Output")
print("====================")

print(
    forecast_df.head(20)
)

# =====================================
# Actual Last Month Output
# =====================================


reference_date = (
    forecast_df["Date"]
    .min()
    - pd.DateOffset(months=1)
)

reference_month = (
    reference_date.month
)

reference_year = (
    reference_date.year
)

actual_last_month_df = product_sales[

    (
        product_sales["Date"]
        .dt.month
        == reference_month
    )

    &

    (
        product_sales["Date"]
        .dt.year
        == reference_year
    )

].copy()

actual_last_month_df = (
    actual_last_month_df

    .rename(
        columns={
            "Name": "Product",
            "Sub_Channels": "Channel",
            "Pricing_Group": "Pricing Group",
            "Required_Qty": "Actual"
        }
    )

    [
        [
            "Date",
            "Product",
            "Channel",
            "Pricing Group",
            "Actual"
        ]
    ]

)
actual_last_month_df = (
    actual_last_month_df
    .groupby(
        [
            "Date",
            "Product",
            "Channel",
            "Pricing Group"
        ]
    )["Actual"]
    .sum()
    .reset_index()
)


actual_last_month_df.to_excel(

    "Actual_Last_Month_Output.xlsx",

    index=False

)

print(
    "\nActual_Last_Month_Output.xlsx Saved Successfully"
)

forecast_df.to_excel(
    "Forecast_Output.xlsx",
    index=False
)

print(
    "\nForecast_Output.xlsx Saved Successfully"
)
