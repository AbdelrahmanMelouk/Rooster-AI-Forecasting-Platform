import streamlit as st
import pandas as pd
import plotly.express as px
import base64

st.set_page_config(
    page_title="Rooster Forecast Dashboard", page_icon="🐓", layout="wide"
)


def get_base64(file_path):

    with open(file_path, "rb") as f:

        return base64.b64encode(f.read()).decode()


bg_base64 = get_base64("BG3.png")
logo_base64 = get_base64("Plogo.png")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ==========================================
# Rooster - Modern Light Login Page
# ==========================================

import streamlit as st

# ---------- Session State ----------
if not st.session_state.logged_in:

    # ---------- Light Theme CSS ----------

    st.markdown(
        f"""
        <style>

        /* ===== Page Background ===== */

        [data-testid="stAppViewContainer"] {{
            background-image:
                linear-gradient(
                    rgba(247, 251, 255, 0.28),
                    rgba(247, 251, 255, 0.28)
                ),
                url("data:image/png;base64,{bg_base64}");

            background-size:  100% 100%;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        [data-testid="stHeader"] {{
            background: transparent;
        }}

        [data-testid="stDecoration"] {{
            display: none;
        }}

        [data-testid="stMain"] {{
            background: transparent;
        }}

        /* ===== Main Layout ===== */

        .block-container {{
            max-width: 100% !important;
            padding-top: 5vh !important;
            padding-bottom: 2rem !important;
        }}

        /* ===== Brand ===== */

        .login-brand {{
        
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 14px;
            margin-bottom: 24px;
        }}
        .login-logo  
        {{
            height: 90px;
            width: auto;
        }}
        

        .login-title {{
            color: #A34700;
            font-size: 60px;
            font-weight: 800;
            letter-spacing: 2px;
            line-height: 1;
            margin: 0;
        }}

        .login-subtitle {{
            color: #7A4A22;
            font-size: 19px;
            font-weight: 500;
            text-align: center;
            margin-top: 10px;
            margin-bottom: 28px;
        }}

        /* ===== Form Card ===== */

        [data-testid="stForm"] {{
    background: rgba(255, 255, 255, 0.76);

    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);

    border: 1px solid rgba(255, 255, 255, 0.85);

    border-radius: 24px;

    padding: 28px 28px 22px 28px;

    box-shadow:
        0 18px 55px rgba(42, 83, 130, 0.15),
        inset 0 1px 0 rgba(255, 255, 255, 0.9);

    transition: all 0.3s ease;
        }}

        /* ===== Input Labels ===== */

        [data-testid="stWidgetLabel"] p {{
            color: #5A3518 !important;
            font-size: 14px !important;
            font-weight: 600 !important;
        }}

        /* ===== Input Fields ===== */

        [data-testid="stTextInput"] input {{
            background: #FFFFFF !important;
            color: #183557 !important;

            border: 1px solid #CAD8EA !important;
            border-radius: 12px !important;

            min-height: 48px !important;
            font-size: 15px !important;

            transition:
                border-color 0.2s ease,
                box-shadow 0.2s ease;
        }}

        [data-testid="stTextInput"] input::placeholder {{
            color: #8495AE !important;
        }}

        [data-testid="stTextInput"] input:focus {{
            border-color: #C65D00 !important;
            box-shadow:
                0 0 0 3px rgba(37, 141, 229, 0.12) !important;
        }}

        /* ===== Login Button ===== */

        [data-testid="stFormSubmitButton"] button {{
            width: 100%;
            min-height: 52px;

            background: linear-gradient(
                110deg,
                #E67E22,
                #A34700
            ) !important;

            color: #FFFFFF !important;
            border: 1px solid #B55300 !important;
            border-radius: 12px !important;

            font-size: 17px !important;
            font-weight: 700 !important;

            box-shadow:
                0 7px 18px rgba(198, 93, 0, 0.25);

            transition: all 0.2s ease;
        }}

        [data-testid="stFormSubmitButton"] button:hover {{
            background: linear-gradient(
                110deg,
                #D66F00,
                #8F3D00
            ) !important;

            box-shadow:
                0 10px 24px rgba(198, 93, 0, 0.35);

            transform: translateY(-1px);
        }}

        /* ===== Footer ===== */

        .login-divider {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-top: 12px;
            margin-bottom: 6px;
        }}


        .login-divider-line {{
            flex: 1;
            height: 1px;
            background: #C7D8E9;
        }}

        .login-divider-leaf {{
            color: #A34700;
            font-size: 19px;
        }}
            .login-footer {{
            color: #7A4A22;
            text-align: center;
            font-size: 17px;
            font-weight: 700;
            margin-top: 0;
            margin-bottom: 30px;
            text-shadow: 0 1px 4px rgba(255,255,255,0.8);
        }}



        /* ===== Alerts ===== */

        [data-testid="stAlert"] {{
            border-radius: 12px;
        }}

        /* ===== Bottom Right Text ===== */

        .bottom-right-note {{
            position: fixed;
            bottom: 18px;
            right: 30px;

            color: #7A4A22;
            font-size: 13px;
            font-weight: 500;

            z-index: 999;
            text-align: right;
            line-height: 1.7;

            text-shadow: 0 1px 3px rgba(255,255,255,0.5);
        }}

        /* ===== Responsive ===== */

        @media (max-width: 768px) {{

            .block-container {{
            max-width: 100% !important;
            padding-top: 2vh !important;
            padding-bottom: 1rem !important;
            }}

            .login-title {{
                font-size: 43px;
            }}

            .login-subtitle {{
                font-size: 15px;
                margin-bottom: 22px;
            }}

            [data-testid="stForm"] {{
                padding: 22px 17px 18px 17px;
                border-radius: 18px;
            }}
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )

    # ---------- Layout ----------

    left, center, right = st.columns([1.15, 1.5, 1.15], gap="small")

    with center:

        # Brand Header
        st.markdown(
            f"""
            <div class="login-brand">
                <img src="data:image/png;base64,{logo_base64}" class="login-logo">
                <span class="login-title">Rooster</span>
            </div>

            """,
            unsafe_allow_html=True,
        )

        # Login Form
        with st.form("Rooster_login_form"):

            email = st.text_input(
                "Company Email", placeholder="Enter your company email"
            )

            password = st.text_input(
                "Password", type="password", placeholder="Enter your password"
            )

            submitted = st.form_submit_button("Login  →", use_container_width=True)

        # Footer
        st.markdown(
            """
            <div class="login-divider">
                <div class="login-divider-line"></div>
                <div class="login-divider-leaf">◆</div>
                <div class="login-divider-line"></div>
            </div>

            <div class="login-footer">
                Secure access for authorized team members
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ---------- Authentication ----------

        if submitted:

            if email.strip().lower().endswith("@rooster.net") and password == "1111":

                st.session_state.logged_in = True
                st.rerun()

            else:

                st.error("Invalid email or password.")

    st.stop()

# =====================================
# Background + Logo Styling
# =====================================


st.markdown(
    f"""
    <style>

    /* =========================
            Dashboard Background
       ========================= */

    .stApp {{
        background-image:
            linear-gradient(
                rgba(255,255,255,0.3),
                rgba(255,255,255,0.3)
            ),
            url("data:image/png;base64,{bg_base64}");

        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* =========================
            Remove White Top Area
       ========================= */

    header {{
        background: transparent !important;
    }}

    [data-testid="stHeader"] {{
        background: transparent !important;
    }}

    [data-testid="stAppViewContainer"] {{
        background: transparent !important;
    }}

    [data-testid="stMain"] {{
        background: transparent !important;
    }}

    .main {{
        background: transparent !important;
    }}

    /* =========================
       Page Layout
       ========================= */

    .block-container {{
        max-width: 100% !important;
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
    }}

    /* =========================
         KPI Cards
       ========================= */

    div[data-testid="stMetric"] 
    {{   
    background: rgba(255, 255, 255, 0.55) !important;
    backdrop-filter: blur(16px) saturate(140%);
    -webkit-backdrop-filter: blur(16px) saturate(140%);
    border: 1px solid rgba(255, 255, 255, 0.7);
    border-left: 6px solid #C65D00;
    border-radius: 20px;
    box-shadow: 0 8px 28px rgba(120, 60, 0, 0.15);

    padding: 28px 32px !important;
    min-height: 140px;
    transition: 0.3s;
    }}

    div[data-testid="stPlotlyChart"] 
    {{    background: rgba(255, 255, 255, 0.60);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(255, 255, 255, 0.7);
    border-radius: 20px;
    padding: 16px;
    box-shadow: 0 8px 28px rgba(120, 60, 0, 0.12);
    }}


    div[data-testid="stDataFrame"] 
    {{
    background: rgba(255, 255, 255, 0.65) !important;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.7);
    border-radius: 18px;
    }}

    div[data-testid="stRadio"] 
        {{  
    background: rgba(255, 255, 255, 0.55);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 16px;
    padding: 12px 16px;
    border: 1px solid rgba(255, 255, 255, 0.7);
        }}
    

    div[data-testid="stMetric"]:hover {{

        transform: translateY(-4px);

        box-shadow:
            0 12px 25px rgba(
                0,
                0,
                0,
                0.15
            );
    }}
    

    /* =========================
        DataFrame
       ========================= */

    div[data-testid="stDataFrame"] {{

        background-color: rgba(
            255,
            255,
            255,
            0.90
        );

        border-radius: 15px;
    }}

    /* =========================
        Select Boxes
       ========================= */

    div[data-baseweb="select"] > div {{

        background: rgba(
            255,
            255,
            255,
            0.90
        ) !important;

        border-radius: 12px;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)
# =====================================
# Load Data
# =====================================


@st.cache_data
def load_data():

    df = pd.read_excel("Forecast_Output.xlsx")

    df["Date"] = pd.to_datetime(df["Date"])

    return df


df = load_data()


@st.cache_data
def load_actual():

    actual_df = pd.read_excel("Actual_Last_Month_Output.xlsx")

    actual_df["Date"] = pd.to_datetime(actual_df["Date"])

    return actual_df


actual_df = load_actual()

# =====================================
# Header
# =====================================

st.markdown(
    """
    <div style="
        background:#C65D00;
        color:white;
        padding:15px;
        border-radius:15px;
        text-align:center;
        font-size:22px;
        font-weight:bold;
        margin-bottom:20px;
        box-shadow:0 4px 12px rgba(0,0,0,0.15);
    ">
        🐓 Rooster AI Forecasting Platform
    </div>
    """,
    unsafe_allow_html=True,
)

logo_col, title_col = st.columns([1, 5])

with logo_col:

   st.image("Plogo.png", width=220)

with title_col:

    st.markdown(
        """
        <h1 style="
            color:#C65D00;
            margin-bottom:0px;
            margin-top:20px;
        ">
            Rooster Demand Forecast Dashboard
        </h1>

        <p style="
            font-size:20px;
            color:#2C2C2C;
            font-weight:600;
            margin-top:0px;
        ">
            Forecast vs Previous Month Actual
        </p>
        """,
        unsafe_allow_html=True,
    )

st.divider()
# =====================================
# Filters
# =====================================

st.markdown(
    """
    <h3 style="
        color:#C65D00;
        margin-bottom:10px;
    ">
    🎯 Forecast Filters
    </h3>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:

    channel = st.selectbox("📢 Channel", sorted(df["Channel"].dropna().unique()))

channel_df = df[df["Channel"] == channel]

with col2:

    pricing = st.selectbox(
        "💰 Pricing Group", sorted(channel_df["Pricing Group"].dropna().unique())
    )

pricing_df = channel_df[channel_df["Pricing Group"] == pricing]
with col3:

    product = st.selectbox(
        "📦 Product", sorted(pricing_df["Product"].dropna().unique())
    )


# =====================================
# Final Filter
# =====================================

filtered_df = df[
    (df["Channel"] == channel)
    & (df["Pricing Group"] == pricing)
    & (df["Product"] == product)
].copy()

filtered_df = filtered_df.sort_values("Date")

if filtered_df.empty:

    st.warning("⚠️ No Data Available For Selected Filters")

    st.stop()
# =====================================
# Actual Last Month
# =====================================

actual_filtered = actual_df[
    (actual_df["Channel"] == channel)
    & (actual_df["Pricing Group"] == pricing)
    & (actual_df["Product"] == product)
].copy()


# =====================================
# Delivery Date Filter
# =====================================

st.markdown(
    """
    <h2 style="
        color:#2C2C2C;
        font-weight:700;
    ">
        📦 Delivery Date
    </h2>
    """,
    unsafe_allow_html=True,
)

date_options = filtered_df["Date"].dt.strftime("%d-%b").tolist()

date_options = ["All Days"] + date_options

selected_date = st.radio("Select Delivery Date", options=date_options, horizontal=True)


# =====================================
# Forecast + Actual Logic
# =====================================
if selected_date == "All Days":

    forecast_value = round(filtered_df["Predicted"].fillna(0).sum())

    forecast_days = filtered_df["Date"].dt.day.tolist()

    actual_value = round(
        actual_filtered[actual_filtered["Date"].dt.day.isin(forecast_days)]["Actual"]
        .fillna(0)
        .sum()
    )

else:

    selected_df = filtered_df[filtered_df["Date"].dt.strftime("%d-%b") == selected_date]

    forecast_value = round(selected_df["Predicted"].fillna(0).sum())

    selected_day = int(selected_date.split("-")[0])

    actual_value = round(
        actual_filtered[actual_filtered["Date"].dt.day == selected_day]["Actual"]
        .fillna(0)
        .sum()
    )


# =====================================
# Growth %
# =====================================

if actual_value > 0:

    growth_pct = round(((forecast_value - actual_value) / actual_value) * 100, 1)

else:

    growth_pct = 0


# =====================================
# KPI Cards
# =====================================

st.divider()
c1, c2, c3 = st.columns(3)

with c1:

    st.metric("AI Suggested Demand", forecast_value)

with c2:

    st.metric("Last Month Actual", actual_value)

with c3:

    st.metric("Growth %", f"{growth_pct}%")
# =====================================
# Forecast Trend
# =====================================

st.divider()

st.subheader("📊 Forecast vs Previous Month Actual")

forecast_chart = filtered_df.copy()

forecast_chart["Day"] = forecast_chart["Date"].dt.day

forecast_days = forecast_chart["Day"].tolist()

actual_chart = actual_filtered[
    actual_filtered["Date"].dt.day.isin(forecast_days)
].copy()

actual_chart["Day"] = actual_chart["Date"].dt.day

actual_chart = actual_chart.groupby("Day")["Actual"].sum().reset_index()

forecast_chart = forecast_chart.groupby("Day")["Predicted"].sum().reset_index()

chart_df = pd.merge(forecast_chart, actual_chart, on="Day", how="outer").fillna(0)

chart_df = chart_df.sort_values("Day")

fig = px.line(
    chart_df,
    x="Day",
    y=["Predicted", "Actual"],
    markers=True,
    color_discrete_sequence=["#C65D00", "#F5A25D"],
)

fig.for_each_trace(
    lambda t: t.update(
        name="Forecast" if t.name == "Predicted" else "Actual Last Month"
    )
)
fig.update_traces(line_width=4, marker_size=10)

fig.update_layout(
    xaxis=dict(
        tickfont=dict(color="#2C2C2C", size=15),
        title_font=dict(color="#2C2C2C", size=18),
    ),
    yaxis=dict(
        tickfont=dict(color="#2C2C2C", size=15),
        title_font=dict(color="#2C2C2C", size=18),
    ),
    font=dict(color="#2C2C2C", size=15),
    title="Forecast vs Previous Month Actual",
    legend_title="",
    xaxis_title="Day Of Month",
    yaxis_title="Quantity",
    height=500,
    plot_bgcolor="rgba(255,255,255,0.95)",
    hovermode="x unified",
    paper_bgcolor="rgba(255,255,255,0)",
)

st.plotly_chart(fig, use_container_width=True)
# =====================================
# Summary Metrics
# =====================================
st.divider()

s1, s2, s3 = st.columns(3)

avg_forecast = round(filtered_df["Predicted"].mean(), 1)

forecast_days = filtered_df["Date"].dt.day.tolist()

avg_actual = round(
    actual_filtered[actual_filtered["Date"].dt.day.isin(forecast_days)][
        "Actual"
    ].mean(),
    1,
)

if avg_actual > 0:

    avg_growth = round(((avg_forecast - avg_actual) / avg_actual) * 100, 1)

else:

    avg_growth = 0

with s1:

    st.metric("AVG Forecast", avg_forecast)

with s2:

    st.metric("AVG Actual", avg_actual)

with s3:

    st.metric("Growth %", f"{growth_pct}%")
# =====================================
# Daily Forecast Table
# =====================================

st.divider()

st.subheader("📋 Daily Forecast Plan")

display_df = filtered_df.copy()

display_df["Date"] = display_df["Date"].dt.strftime("%Y-%m-%d")

display_df["Predicted"] = display_df["Predicted"].round(0).astype(int)

st.dataframe(display_df, use_container_width=True)

# =====================================
# Download Forecast
# =====================================

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Forecast",
    data=csv,
    file_name="Forecast_Output.csv",
    mime="text/csv",
)

# =====================================
# Footer
# =====================================

st.divider()

st.markdown(
    """
    <div style="
        text-align:center;
        color:#FFFFFF;
        font-weight:700;
        font-size:15px;
        padding-bottom:15px;
        text-shadow:0px 2px 4px rgba(0,0,0,0.5);
    ">
        © Rooster AI Forecasting Platform | Weekly Demand Prediction Engine
    </div>
    """,
    unsafe_allow_html=True,
)
