import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return 23*x**2 + 9*x + 18

st.write('INTEGRAL TRAPESIUM UNTUK FUNGSI F(X)= 23x**2 + 9x + 18')

x = st.slider('Select range', -2.0, 2.0, (0.2, 0.5))
st.write('Selected range:', x)

# Calculate the values of the function
t = np.linspace(x[0], x[1], 100)
u = f(t)

# Calculate the integral using the trapezoidal rule
integral = np.trapz(u, t)

st.write('Integral using trapezoidal rule:', integral)

# Plot the function
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(t, u, label='f(x) = 23x^2 + 9x + 18', color='b')
ax.fill_between(t, u, color='skyblue', alpha=0.3)
ax.set_ylabel("f(x)")
ax.set_xlabel("x")
ax.tick_params(axis='both', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=0.5)
st.pyplot(fig)
