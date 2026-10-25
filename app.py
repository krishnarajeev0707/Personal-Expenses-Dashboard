# Streamlit run command is to be used in CMD Prompt with Appropriate file name and directory(if it doesn't work with pip)


# Importing Modules required
import streamlit as st                 # StreamLit  : GUI
import pandas as pd                    # Pandas     : Data Processing
import matplotlib.pyplot as plt        # MatPlotLib : Graphs

# Main Page Configuration
st.set_page_config(
    page_title="Personal Dashboard",
    layout="wide",
)

# Basic Styling Using CSS 
# (External Reference for Gradient cards)
st.markdown("""
<style>
body, .stApp {
    font-family: 'Bahnschrift';
    background: #0b0c10;
}
/* DARK 3D GRADIENT CARD */
.gradient-card {
    font-family: 'Bahnschrift';
    background: linear-gradient(135deg, #1c1f24 0%, #0b0c10 100%);
    border-radius: 16px;
    padding: 25px;
    color: #e8e8e8;
    box-shadow:
        4px 4px 12px rgba(0,0,0,0.7),
        -3px -3px 8px rgba(70,70,70,0.08);
    border: 1px solid rgba(255,255,255,0.04);
    transition: 0.2s ease;
}
.gradient-card h3 {
    margin: 0;
    font-family: 'Bahnschrift';
    font-size: 22px;
    font-weight: 600;
}
.gradient-card h2 {
    margin-top: 10px;
    font-family: 'Bahnschrift';
    font-size: 32px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# Loading and Preprocessing Dataset
@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    df.columns = df.columns.str.strip().str.title()
    rename_map = {
        "Transaction Date": "Date",
        "Expense": "Amount",
        "Value": "Amount",
        "Expenses/Income": "Type",
        "Income/Expense": "Type"}
    df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns}, inplace=True)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df.dropna(subset=["Date", "Amount"], inplace=True)
    if "Type" in df.columns:
        df["Type"] = df["Type"].astype(str).str.strip().str.lower()
        df.loc[df["Type"] == "income", "Amount"] *= -1
    df["Month"] = df["Date"].dt.month_name()
    df["MonthNum"] = df["Date"].dt.month
    return df

# Main Title (Centered using CSS)
st.markdown("<h1 style='text-align:center; color:white;'>Personal Expense Dashboard</h1>", unsafe_allow_html=True)
st.markdown("")            # To even out spacing below title

# File Uploader
with st.container(border=True):
    st.markdown("#### Upload your bank statement CSV", unsafe_allow_html=True)
    uploaded = st.file_uploader("", type=["csv"])
    if not uploaded:
        st.info("Please upload a CSV to continue.")
        st.stop()
    st.markdown("")
df = load_data(uploaded)

# Calculations for Summary Cards
df_exp = df[df["Amount"] > 0]
total = df["Amount"].sum()
income_total = df[df["Amount"] < 0]["Amount"].sum() * -1
expense_total = df_exp["Amount"].sum()

# Summary Cards
col1, col2, col3 = st.columns(3)
with col1:                          # Card1 : Total Expenses
    st.markdown(f"""
        <div class="gradient-card">
            <h3>Total Expenses</h3>
            <h2 style="color:#ff4d4d;">₹{expense_total:,.2f}</h2>
        </div>
    """, unsafe_allow_html=True)
with col2:                          # Card2 : Total Income
    st.markdown(f"""
        <div class="gradient-card">
            <h3>Total Income</h3>
            <h2 style="color:#2ecc71;">₹{income_total:,.2f}</h2>
        </div>
    """, unsafe_allow_html=True)
with col3:                          # Card3 : Balance Change
    st.markdown(f"""
        <div class="gradient-card">
            <h3>Net Balance Change</h3>
            <h2 style="color:#3498db;">₹{total:,.2f}</h2>
        </div>
    """, unsafe_allow_html=True)
st.markdown("")

# Filters
with st.container(border=True):
    st.markdown("### Filters", unsafe_allow_html=True)
    colA, colB = st.columns(2)
    with colA:
        category = st.selectbox("Filter by Category", ["All"] + sorted(df["Category"].unique()))
    with colB:
        month = st.selectbox("Filter by Month", ["All"] + sorted(df["Month"].unique()))
    st.markdown("")
    filtered = df.copy()
    if category != "All":
        filtered = filtered[filtered["Category"] == category]
    if month != "All":
        filtered = filtered[filtered["Month"] == month]
    st.dataframe(filtered, use_container_width=True)

# Analytics 
with st.container(border=True):
    st.markdown("### Analytics", unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["Category Breakdown", "Monthly Trend", "Data Table"])

with tab1:                    # Tab 1: Category-wise Breakdown: Bar graph
    st.markdown("### Category-wise Breakdown")
    st.markdown("")
    cat_totals = df_exp.groupby("Category")["Amount"].sum()
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    fig1.patch.set_facecolor("#0b0c10")
    ax1.set_facecolor("#0b0c10")
    ax1.bar(cat_totals.index, cat_totals.values)
    ax1.grid(True, color="gray", axis="y", linestyle="--", linewidth=0.5, alpha=0.4)
    ax1.tick_params(colors="white", rotation=45)
    ax1.set_title("Category Breakdown", color="white")
    ax1.set_ylabel("Amount", color="white")
    for spine in ax1.spines.values():
        spine.set_color("white")
    st.pyplot(fig1)
    st.markdown("")

with tab2:                  # Tab 2: Monthly Expense Trend: Line Chart
    st.markdown("### Monthly Expense Trend")
    st.markdown("")
    monthly_exp = (
        df_exp.groupby(["MonthNum", "Month"])["Amount"].sum().reset_index().sort_values("MonthNum"))
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    fig2.patch.set_facecolor("#0b0c10")
    ax2.set_facecolor("#0b0c10")
    ax2.plot(monthly_exp["Month"], monthly_exp["Amount"], 
            linestyle="dotted", marker="o", linewidth=2,)
    ax2.grid(True, color="gray", axis="y", linestyle="--", linewidth=0.5, alpha=0.4)
    ax2.tick_params(colors="white", rotation=45)
    ax2.set_title("Monthly Expense Trend", color="white")
    ax2.set_ylabel("Amount", color="white")
    for spine in ax2.spines.values():
        spine.set_color("white")
    st.pyplot(fig2)
    st.markdown("")

with tab3:                  # Tab 3: Cleaned Dataset
    st.markdown("")
    st.dataframe(filtered, use_container_width=True)

# Balance Calculator
with st.container(border=True):
    st.markdown("### Balance Calculator", unsafe_allow_html=True)
    starting = st.number_input("Enter Starting Balance", value=10000)
    final_bal = starting - total
    st.success(f"**Final Balance: ₹{final_bal:,.2f}**")
    st.markdown("")