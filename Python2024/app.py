import streamlit as st # interface web
import pandas as pd # manipulação de dados

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/customer_reviews.csv")
df_top100_books = pd.read_csv("datasets/customer_reviews.csv")

df_reviews