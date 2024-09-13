# Projectile-Motion-Simulator

Welcome to the Projectile Motion Simulator! This Streamlit-based web app allows you to visualize the trajectory of a projectile based on various initial conditions and planetary environments.

## App Features
* Interactive Sliders: Adjust the initial velocity and launch angle of the projectile.
* Planet Selection: Choose from different planets to see how their gravity affects the projectile's path.
* Dynamic Plot: View the static plot of the projectile’s trajectory as influenced by your inputs.

## How to Use
Open the App: Access the app via the following URL: [Projectile Motion Simulator](https://projectile-motion-simulator.streamlit.app/).

## Input Parameters:

* Initial Velocity (m/s): Use the slider to set the initial velocity of the projectile.
*Launch Angle (degrees): Adjust the slider to select the angle at which the projectile is launched.
* Select the Planet: Choose the planet from the dropdown menu. This selection affects the gravitational force acting on the projectile.

## Run the Simulation:
Click the `Start Simulation` button to generate and view the projectile's trajectory.
View the Results:

The app will display a static plot showing the path of the projectile based on your inputs. The plot will update according to the selected initial conditions and planetary environment.

## About the App
This app is built using Streamlit and Matplotlib. It calculates the trajectory of a projectile given: Initial velocity, Launch angle, Gravitational acceleration (depending on the selected planet)

## Technologies Used
* Streamlit: A framework for creating interactive web applications in Python.
* Matplotlib: A plotting library for creating static, animated, and interactive visualizations in Python.
* NumPy: A library for numerical operations in Python.

## How It Works
* Calculate Trajectory: The app calculates the projectile's trajectory using the equations of motion.
* Plot the Path: It then plots the trajectory on a graph using Matplotlib.
* Display in Streamlit: Finally, the plot is rendered within the Streamlit interface for user interaction.


## License
This project is licensed under the MIT License - see the [LICENSE](LISCENSE.txt) file for details.
