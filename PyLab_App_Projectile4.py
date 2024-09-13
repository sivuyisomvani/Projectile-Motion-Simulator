import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Dictionary of planets with their gravitational constants
planets = {
    'Earth': 9.81,      # Earth's gravity in m/s^2
    'Mars': 3.71,       # Mars' gravity in m/s^2
    'Moon': 1.62,       # Moon's gravity in m/s^2
    'Jupiter': 24.79    # Jupiter's gravity in m/s^2
}

def calculate_trajectory(v0, theta, g, t_end=10):
    """Calculate the projectile trajectory given initial velocity, angle, and gravity."""
    theta_rad = np.radians(theta)
    t = np.linspace(0, t_end, num=500)
    
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2
    
    return x, y

# Streamlit app layout
st.title('Projectile Motion Simulator')

# User inputs via sliders and multi-select
v0 = st.slider('Initial Velocity (m/s)', 0, 100, 50)  # Velocity slider
theta = st.slider('Launch Angle (degrees)', 0, 90, 45)  # Angle slider
selected_planet = st.selectbox('Select the Planet', options=list(planets.keys()))  # Planet selection

# Button to start the simulation
start_simulation = st.button('Start Simulation')

if start_simulation:
    # Retrieve the gravity of the selected planet
    g = planets[selected_planet]
    
    # Calculate trajectory
    x, y = calculate_trajectory(v0, theta, g)
    
    # Set up plot
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Trajectory")
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Height (m)')
    ax.set_title(f'Projectile Motion on {selected_planet}')
    ax.legend()
    
    # Display plot in the Streamlit app
    st.pyplot(fig)
