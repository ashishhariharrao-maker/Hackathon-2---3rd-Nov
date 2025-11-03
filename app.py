import streamlit as st
import pickle

# Load the model
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

st.title("My ML Prediction App")

# Get user input
input_feature_1 = st.number_input("Feature 1")
input_feature_2 = st.number_input("Feature 2")

if st.button("Predict"):
# Make prediction
    prediction = loaded_model.predict([[input_feature_1, input_feature_2]])
    st.write(f"The prediction is: {prediction[0]}")
    
#if __name__ == "__main__":
       # app.run(debug=True)