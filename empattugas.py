import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return 23*x**2 + 9*x + 18

# Slider for choosing the range of x values
x_range = st.slider('Choose the range of x', 0.0, 2.0, (0.2, 0.5))

# Slider for setting the value of y
y = st.slider('Set the value of y', 0.0, 100.0, 25.0)

# Calculate the values of x and f(x)
x_values = np.linspace(x_range[0], x_range[1], 100)
f_values = f(x_values)

# Calculate the integral using the trapezoidal rule
integral = np.trapz(f_values, x_values)

# Plot the function
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x_values, f_values, label='$23x^2 + 9x + 18$', color='b')
ax.fill_between(x_values, f_values, color='skyblue', alpha=0.4)
ax.set_ylabel("f(x)")
ax.set_xlabel("x")
ax.tick_params(axis='both', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=0.5)

# Display the integral value
st.write('Integral using the trapezoidal rule:', integral)

# Display the plot
st.pyplot(fig)
