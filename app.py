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
year = st.number_input("Release Year", min_value=1980, max_value=2025, step=1)
platform = st.number_input("Platform (Encoded)", min_value=0)
genre = st.number_input("Genre (Encoded)", min_value=0)
publisher = st.number_input("Publisher (Encoded)", min_value=0)

na_sales = st.number_input("NA Sales (in millions)", min_value=0.0, step=0.01)
eu_sales = st.number_input("EU Sales (in millions)", min_value=0.0, step=0.01)
jp_sales = st.number_input("JP Sales (in millions)", min_value=0.0, step=0.01)
other_sales = st.number_input("Other Sales (in millions)", min_value=0.0, step=0.01)


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
