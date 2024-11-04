import requests
import streamlit as st

data = requests.get("https://apexapps.oracle.com/pls/apex/cetools/api/v1/products").json()

st.write(data)