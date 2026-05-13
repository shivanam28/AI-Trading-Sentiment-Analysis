import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Bitcoin Sentiment vs Trader Performance")

df = pd.read_csv("merged_data.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Average PnL by Sentiment")

avg_pnl = df.groupby('classification')['Closed PnL'].mean()

fig, ax = plt.subplots()

avg_pnl.plot(kind='bar', ax=ax)

st.pyplot(fig)

st.subheader("Trade Size Analysis")

trade_size = df.groupby('classification')['Size USD'].mean()

fig, ax = plt.subplots()

trade_size.plot(kind='bar', ax=ax)

st.pyplot(fig)

st.subheader("Win Rate Analysis")

df['profit_flag'] = df['Closed PnL'] > 0

win_rate = df.groupby(
    'classification'
)['profit_flag'].mean() * 100

fig, ax = plt.subplots()

win_rate.plot(kind='bar', ax=ax)

st.pyplot(fig)