# =========================================
# IMPORTS
# =========================================
import streamlit as st
import numpy as np
import pickle

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="Video Game Sales Predictor",
    page_icon="🎮",
    layout="wide"
)

# =========================================
# LOAD MODEL & FILES
# =========================================
@st.cache_resource
def load_files():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("encoders.pkl", "rb") as f:
        encoders = pickle.load(f)

    with open("features.pkl", "rb") as f:
        features = pickle.load(f)

    return model, encoders, features

model, encoders, feature_order = load_files()

# =========================================
# CUSTOM STYLING (DARK MODERN UI)
# =========================================
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.block-container {
    padding-top: 2rem;
}
.stNumberInput input, .stSelectbox div {
    background-color: #1e1e2f !important;
    color: white !important;
    border-radius: 10px !important;
}
.stButton button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    font-size: 18px;
    background: linear-gradient(90deg, #6a11cb, #2575fc);
    color: white;
}
.stButton button:hover {
    background: linear-gradient(90deg, #2575fc, #6a11cb);
}
</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================
st.markdown("""
<h1 style='text-align: center;'>🎮 Video Game Global Sales Predictor</h1>
<p style='text-align: center; color: gray;'>
Predict global sales using machine learning
</p>
""", unsafe_allow_html=True)

st.divider()

# =========================================
# INPUT SECTION
# =========================================
col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Release Year", 1980, 2025, step=1)

    platform_name = st.selectbox(
        "Platform",
        encoders['platform'].classes_
    )

    genre_name = st.selectbox(
        "Genre",
        encoders['genre'].classes_
    )

with col2:
    publisher_name = st.selectbox(
        "Publisher",
        encoders['publisher'].classes_
    )

    na_sales = st.number_input("NA Sales", min_value=0.0, step=0.1)
    eu_sales = st.number_input("EU Sales", min_value=0.0, step=0.1)

# Bottom row
col3, col4 = st.columns(2)

with col3:
    jp_sales = st.number_input("JP Sales", min_value=0.0, step=0.1)

with col4:
    other_sales = st.number_input("Other Sales", min_value=0.0, step=0.1)

# =========================================
# ENCODE INPUTS
# =========================================
try:
    platform = encoders['platform'].transform([platform_name])[0]
    genre = encoders['genre'].transform([genre_name])[0]
    publisher = encoders['publisher'].transform([publisher_name])[0]
except Exception as e:
    st.error("Encoding error. Check encoder files.")
    st.stop()

# =========================================
# PREDICTION BUTTON
# =========================================
if st.button("🚀 Predict Global Sales"):

    # Input validation
    if na_sales + eu_sales + jp_sales + other_sales == 0:
        st.warning("⚠️ Sales values cannot all be zero")
        st.stop()

    # Prepare input dictionary
    input_dict = {
        'platform': platform,
        'year': year,
        'genre': genre,
        'publisher': publisher,
        'na_sales': na_sales,
        'eu_sales': eu_sales,
        'jp_sales': jp_sales,
        'other_sales': other_sales
    }

    # Maintain correct feature order
    try:
        input_data = np.array([[input_dict[col] for col in feature_order]])
    except KeyError:
        st.error("Feature mismatch between model and app.")
        st.stop()

    # Prediction
    prediction = model.predict(input_data)[0]

    # =========================================
    # RESULT DISPLAY (CARD STYLE)
    # =========================================
    st.markdown(f"""
        <div style='
            background: linear-gradient(90deg, #11998e, #38ef7d);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            color: black;
        '>
        🌍 Predicted Global Sales: {prediction:.2f} million units
        </div>
    """, unsafe_allow_html=True)

    # =========================================
    # OPTIONAL: SALES BREAKDOWN CHART
    # =========================================
    st.subheader("📊 Regional Sales Breakdown")

    st.bar_chart({
        "Sales": [
            na_sales,
            eu_sales,
            jp_sales,
            other_sales
        ]
    })

# =========================================
# FOOTER
# =========================================
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Built with Streamlit 🚀</p>",
    unsafe_allow_html=True
)