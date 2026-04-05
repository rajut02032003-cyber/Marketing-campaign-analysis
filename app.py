import streamlit as st
import pandas as pd

st.title("Marketing Campaign Dashboard")

df = pd.read_csv("cleaned_data.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Selected Columns Data")
st.dataframe(df)

st.sidebar.header("Filters")

education = st.sidebar.selectbox("Education", df["Education"].unique())
country = st.sidebar.selectbox("Country", df["Country"].unique())

filtered_df = df[(df["Education"] == education) & (df["Country"] == country)]

st.subheader("Filtered Data")
st.dataframe(filtered_df)

st.subheader("Key Metrics")

st.metric("Total Customers", len(filtered_df))
st.metric("Average Income", int(filtered_df["Income"].mean()))

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(filtered_df["Income"])

st.subheader("Income Distribution")
st.pyplot(fig)


spending = filtered_df[[
    'MntWines','MntFruits','MntMeatProducts',
    'MntFishProducts','MntSweetProducts','MntGoldProds'
]].sum()

st.subheader("Product Spending")
st.bar_chart(spending)


purchases = filtered_df[[
    'NumWebPurchases','NumStorePurchases','NumCatalogPurchases'
]].sum()

st.subheader("Purchase Channels")
st.bar_chart(purchases)


st.subheader("Insights")

st.write("Customers with higher income tend to spend more on wines and meat products.")
st.write("Web purchases are higher compared to catalog purchases.")