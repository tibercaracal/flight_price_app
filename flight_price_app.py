import streamlit as st
import pandas as pd
import scikit-learn
import joblib

# Load trained model
model = joblib.load("flight_price_model_latest_v2.pkl")

# Define dropdown options
airlines = ['SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India']
cities = ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai']
departure_times = ['Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night']
arrival_times = ['Night', 'Morning', 'Early_Morning', 'Afternoon', 'Evening', 'Late_Night']
stops_options = ['zero', 'one', 'two_or_more']
classes = ['Economy', 'Business']

st.title("✈️ Flight Price Predictor")

# User input form
airline = st.selectbox("Airline", airlines)
source_city = st.selectbox("Source City", cities)
destination_city = st.selectbox("Destination City", cities)
departure_time = st.selectbox("Departure Time", departure_times)
arrival_time = st.selectbox("Arrival Time", arrival_times)
stops = st.selectbox("Number of Stops", stops_options)
flight_class = st.selectbox("Flight Class", classes)
duration = st.number_input("Flight Duration (hours)", min_value=0.0, step=0.1)
days_left = st.number_input("Days Left Until Departure", min_value=0, step=1)

# Prediction
if st.button("Predict Flight Price"):
    input_data = pd.DataFrame({
        "airline": [airline],
        "source_city": [source_city],
        "departure_time": [departure_time],
        "stops": [stops],
        "arrival_time": [arrival_time],
        "destination_city": [destination_city],
        "flight_class": [flight_class],
        "duration": [duration],
        "days_left": [days_left]
    })

    prediction = model.predict(input_data)
    st.success(f"Estimated Flight Price: ₹{prediction[0]:,.0f}")
