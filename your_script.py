import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Sales Report Dashboard")

df = pd.read_csv("10000 Sales Records.csv")
st.write("Data shape:", df.shape)
st.write("Missing values:", df.isnull().sum())

# Top Products
top_products = df.groupby('Item Type')['Total Revenue'].sum().sort_values(ascending=False).head(10)
fig1, ax1 = plt.subplots()
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis', ax=ax1)
ax1.set_title('Top 10 Products by Total Revenue')
st.pyplot(fig1)

# Region Sales
region_sales = df.groupby('Region')['Total Revenue'].sum().sort_values()
fig2, ax2 = plt.subplots()
region_sales.plot(kind='barh', color='skyblue', ax=ax2)
ax2.set_title('Total Revenue by Region')
st.pyplot(fig2)

# Monthly Trend
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Month'] = df['Order Date'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Total Revenue'].sum()
    fig3, ax3 = plt.subplots()
    monthly_sales.plot(marker='o', linestyle='-', color='teal', ax=ax3)
    ax3.set_title('Monthly Sales Trend')
    st.pyplot(fig3)