import streamlit as st # interface web
import pandas as pd # manipulação de dados


df_reviews = pd.read_csv('datasets/')
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

df_reviewss