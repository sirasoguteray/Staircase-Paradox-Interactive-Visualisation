import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

# Initial parameters
base_length = 4  # Fixed base of the triangle
vertical_height = 3  # Fixed height of the triangle
steps = 1  # Start with one step

# Function to draw the staircase paradox
def draw_staircase(steps):
    """
    Draws the staircase and the original triangle on the plot.

    Parameters:
        steps (int): The number of steps in the staircase.
    """
    # X and Y coordinates for the staircase
    x = [0]
    y = [0]

    # Calculate the dimensions of each step
    step_length = base_length / steps
    step_height = vertical_height / steps

    # Generate staircase points
    for _ in range(steps):
        x.append(x[-1] + step_height)  # Add horizontal step
        y.append(y[-1])               # Maintain same height
        x.append(x[-1])
        y.append(y[-1] + step_length) # Add vertical step

    # Clear the plot but keep the original triangle
    ax.clear()
    # Plot the original triangle
    ax.plot([0, 3, 3, 0], [0, 0, 4, 0], linestyle='-', color='g', label="Original Triangle")

    # Plot the staircase
    ax.plot(x, y, marker='o', linestyle='-', color='b', label="Staircase")
    ax.set_title(f"Staircase Paradox - {steps} Steps")
    ax.set_xlabel("Horizontal Distance")
    ax.set_ylabel("Vertical Distance")

    # Draw the original hypotenuse for comparison
    ax.plot([0, vertical_height], [0, base_length], linestyle='--', color='r', label="Original Hypotenuse")

    # Add legend and grid
    ax.legend()
    ax.grid()
    ax.axis("equal")

    # Add contact information to the corner
    ax.text(0.5, -0.2, "Eray Sırasöğüt - eraysirasogut@gmail.com", transform=ax.transAxes,
            fontsize=8, color='gray', ha='center', va='top')

    plt.draw()

# Function to handle button click to add steps
def add_step(event):
    """Increases the number of steps in the staircase by 1."""
    global steps
    steps += 1
    draw_staircase(steps)

# Function to handle button click to remove steps
def remove_step(event):
    """Decreases the number of steps in the staircase by 1 if steps > 1."""
    global steps
    if steps > 1:
        steps -= 1
    draw_staircase(steps)

# Function to handle button click to reset steps
def reset_steps(event):
    """Resets the number of steps in the staircase to 1."""
    global steps
    steps = 1
    draw_staircase(steps)

# Create the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.4)  # Adjust bottom space for buttons

# Initial drawing of the staircase and triangle
draw_staircase(steps)

# Add a button to add steps
ax_add_button = plt.axes([0.2, 0.05, 0.2, 0.075])
add_button = Button(ax_add_button, 'Add Step')
add_button.on_clicked(add_step)

# Add a button to remove steps
ax_remove_button = plt.axes([0.45, 0.05, 0.2, 0.075])
remove_button = Button(ax_remove_button, 'Remove Step')
remove_button.on_clicked(remove_step)

# Add a button to reset steps
ax_reset_button = plt.axes([0.7, 0.05, 0.2, 0.075])
reset_button = Button(ax_reset_button, 'Reset Steps')
reset_button.on_clicked(reset_steps)

plt.show()