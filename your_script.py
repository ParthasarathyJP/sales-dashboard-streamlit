import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🪔 Title and Introduction
st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Report Dashboard")
st.markdown("🦉 *Audit Owl says: 'Let no one wear your badge without earning it—these top products earned their scrolls through sovereign sales!'*")

# 📂 Load Data
df = pd.read_csv("Sales Records.csv")

# 🎛️ Sidebar Filters
st.sidebar.header("🔍 Filter Options")
regions = df['Region'].unique()
selected_region = st.sidebar.selectbox("Select Region", options=regions)
filtered_df = df[df['Region'] == selected_region]

# 📊 Tabs for Visual Sections
tab1, tab2, tab3 = st.tabs(["Top Products", "Region Sales", "Monthly Trend"])

# 🎯 Top Products by Revenue
with tab1:
    st.subheader(f"Top 10 Products in {selected_region}")
    top_products = filtered_df.groupby('Item Type')['Total Revenue'].sum().sort_values(ascending=False).head(10)
    fig1, ax1 = plt.subplots()
    sns.barplot(x=top_products.values, y=top_products.index, palette='viridis', ax=ax1)
    ax1.set_title('Top 10 Products by Total Revenue')
    st.pyplot(fig1)

# 🌍 Region Sales Overview
with tab2:
    st.subheader("Total Revenue by Region")
    region_sales = df.groupby('Region')['Total Revenue'].sum().sort_values()
    fig2, ax2 = plt.subplots()
    ax2.barh(region_sales.index, region_sales.values, color='skyblue')
    ax2.set_title('Total Revenue by Region')
    st.pyplot(fig2)

# 📅 Monthly Sales Trend
with tab3:
    st.subheader(f"Monthly Sales Trend in {selected_region}")
    if 'Order Date' in filtered_df.columns:
        filtered_df['Order Date'] = pd.to_datetime(filtered_df['Order Date'])
        filtered_df['Month'] = filtered_df['Order Date'].dt.to_period('M')
        monthly_trend = filtered_df.groupby('Month')['Total Revenue'].sum()
        fig3, ax3 = plt.subplots()
        ax3.plot(monthly_trend.index.to_timestamp(), monthly_trend.values, marker='o', linestyle='-', color='teal')
        ax3.set_title('Monthly Sales Trend')
        st.pyplot(fig3)
    else:
        st.warning("🕰️ 'Order Date' column not found in dataset.")