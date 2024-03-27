import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load data
@st.cache
def load_data():
    return pd.read_csv('Heart_Disease_Prediction.csv')

df = load_data()

# Display data
st.subheader('Data')
st.write(df.head())
st.write(df.info())

# Data visualization
st.subheader('Data Visualization')

# Display count plot
st.write(sns.countplot(x=df['Heart Disease'], hue='Sex', data=df))

# Display other plots here...

# Split data
X = df.drop(columns=['Heart Disease'])
y = df['Heart Disease'].map({'Presence': 1, 'Absence': 0})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build model
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), verbose=2)

# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
st.write(f"Test Accuracy: {accuracy}")

# New data prediction
st.subheader('New Data Prediction')

new_data = np.array([[32, 1, 2, 115, 260, 1, 0, 170, 1, 1.6, 1, 0, 3]])
new_data_scaled = scaler.transform(new_data)

predictions = model.predict(new_data_scaled)
binary_predictions = (predictions > 0.5).astype(int)

st.write(f"Predicted Probability: {predictions[0][0]}")
st.write(f"Binary Prediction: {binary_predictions[0][0]}")
if binary_predictions == 0:
    st.write("Absence")
else:
    st.write("Presence")
