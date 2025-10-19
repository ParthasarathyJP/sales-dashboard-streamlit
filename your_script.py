import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Report Dashboard")

# 📂 Load CSV
df = pd.read_csv("Sales Records.csv")

# 🎯 Top 10 Products by Revenue
top_products = df.groupby('Item Type')['Total Revenue'].sum().sort_values(ascending=False).head(10).reset_index()
fig1 = px.bar(top_products, x='Total Revenue', y='Item Type', orientation='h', color='Item Type',
              title='Top 10 Products by Total Revenue')
st.plotly_chart(fig1)

# 🌍 Region Sales
region_sales = df.groupby('Region')['Total Revenue'].sum().sort_values(ascending=False).reset_index()
fig2 = px.bar(region_sales, x='Region', y='Total Revenue', color='Region', title='Total Revenue by Region')
st.plotly_chart(fig2)

# 📅 Monthly Sales Trend
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Month'] = df['Order Date'].dt.to_period('M').astype(str)
    monthly_sales = df.groupby('Month')['Total Revenue'].sum().reset_index()
    fig3 = px.line(monthly_sales, x='Month', y='Total Revenue', markers=True, title='Monthly Sales Trend')
    st.plotly_chart(fig3)