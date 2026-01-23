# -*- coding: utf-8 -*-
"""
Video Game Global Sales Prediction App
"""

import streamlit as st
import numpy as np
import pickle

# Load Trained Model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# App UI
st.set_page_config(page_title="Video Game Sales Predictor", layout="centered")

st.title("🎮 Video Game Global Sales Predictor")
st.markdown("Predict **Global Sales** of a video game using Linear Regression")

st.divider()

# User Inputs
rank = st.number_input("Game Rank", min_value=1, step=1)
year = st.number_input("Release Year", min_value=1980, max_value=2025, step=1)
platform = st.number_input("Platform (Encoded)", min_value=0)
genre = st.number_input("Genre (Encoded)", min_value=0)
publisher = st.number_input("Publisher (Encoded)", min_value=0)

na_sales = st.number_input("NA Sales", min_value=0.0)
eu_sales = st.number_input("EU Sales", min_value=0.0)
jp_sales = st.number_input("JP Sales", min_value=0.0)
other_sales = st.number_input("Other Sales", min_value=0.0)



# Prediction
if st.button("Predict Global Sales 🚀"):
    input_data = np.array([[
        year,
        platform,
        genre,
        publisher,
        na_sales,
        eu_sales,
        jp_sales,
        other_sales
    ]])

    prediction = model.predict(input_data)

    st.success(f"🌍 Predicted Global Sales: **{prediction[0]:.2f} million units**")
