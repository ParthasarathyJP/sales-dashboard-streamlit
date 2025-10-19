import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Report Dashboard")

# 📂 Load CSV
df = pd.read_csv("Sales Records.csv")

# 🎯 Top 10 Products by Revenue
top_products = df.groupby('Item Type')['Total Revenue'].sum().sort_values(ascending=False).head(10).reset_index()
bar_chart = alt.Chart(top_products).mark_bar().encode(
    x='Total Revenue',
    y=alt.Y('Item Type', sort='-x'),
    color='Item Type'
).properties(title='Top 10 Products by Total Revenue')
st.altair_chart(bar_chart, use_container_width=True)

# 🌍 Region Sales
region_sales = df.groupby('Region')['Total Revenue'].sum().sort_values(ascending=False).reset_index()
region_chart = alt.Chart(region_sales).mark_bar().encode(
    x='Total Revenue',
    y=alt.Y('Region', sort='-x'),
    color='Region'
).properties(title='Total Revenue by Region')
st.altair_chart(region_chart, use_container_width=True)

# 📅 Monthly Sales Trend
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Month'] = df['Order Date'].dt.to_period('M').astype(str)
    monthly_sales = df.groupby('Month')['Total Revenue'].sum().reset_index()
    line_chart = alt.Chart(monthly_sales).mark_line(point=True).encode(
        x='Month',
        y='Total Revenue'
    ).properties(title='Monthly Sales Trend')
    st.altair_chart(line_chart, use_container_width=True)