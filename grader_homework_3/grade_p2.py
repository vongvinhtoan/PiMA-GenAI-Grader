import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from .dual_number import *

# Define the function
def f(x, y):
    exp1 = exp(-((x**2 + y**2)/4 + (1/4)*x*y))
    exp2 = exp(-((x**2 + y**2)/4 - (1/4)*x*y))
    return sin(3 * exp1)**2 + sin(3 * exp2)**2

def f_derivative(x, y) -> tuple[float, float]:
    """
    Calculate the gradient of the function f at (x, y). Using dual numbers.
    
    Args:
        x (float): x-coordinate.
        y (float): y-coordinate.
        
    Returns:
        tuple[float, float]: Gradient vector (df/dx, df/dy).
    """
    f_x = f(Dual(x, 1), Dual(y, 0))
    f_y = f(Dual(x, 0), Dual(y, 1))
    return f_x.dual, f_y.dual

def plot_function_conture():
    # Create a grid of x, y values
    x = np.linspace(-4, 4, 400)
    y = np.linspace(-4, 4, 400)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # Plot the contour
    plt.figure(figsize=(8, 6))
    contours = plt.contour(X, Y, Z, levels=10, cmap='inferno')
    plt.clabel(contours, inline=True, fontsize=8)
    plt.title("Contour Plot of Custom Function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axis("equal")
    plt.show()

def plot_function_derivative_vector_field():
    # Create a grid of x, y values
    x = np.linspace(-4, 4, 20)
    y = np.linspace(-4, 4, 20)
    X, Y = np.meshgrid(x, y)

    # Compute the vector field components
    U, V = f_derivative(X, Y)

    # Compute magnitude for coloring
    magnitude = np.sqrt(U**2 + V**2)

    plt.figure(figsize=(8, 6))
    # Use quiver with coloring by magnitude
    quiver = plt.quiver(X, Y, U, V, magnitude, cmap='plasma', scale=40)
    plt.colorbar(quiver, label='Magnitude')
    plt.title("Vector Field of f(x, y)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axis("equal")
    plt.show()

def plot_samples_with_contour(samples):
    x_samples, y_samples = zip(*samples)

    # --- Grid and Contour ---
    x = y = np.linspace(-4, 4, 400)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    fig = plt.figure(figsize=(14, 6))
    gs = gridspec.GridSpec(1, 3, width_ratios=[1, 1, 0.05], wspace=0.2)

    # Left: Heatmap only
    ax1 = fig.add_subplot(gs[0])
    _, _, _, img1 = ax1.hist2d(x_samples, y_samples, bins=200, cmap='viridis', alpha=0.8)
    ax1.set_title("Heatmap of Sampled Points")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_aspect("equal", adjustable="box")
    ax1.grid(True)

    # Right: Heatmap + Contours
    ax2 = fig.add_subplot(gs[1])
    _, _, _, img2 = ax2.hist2d(x_samples, y_samples, bins=200, cmap='viridis', alpha=0.8)
    contours = ax2.contour(X, Y, Z, levels=10, linewidths=1, cmap='inferno')
    ax2.clabel(contours, inline=True, fontsize=8)
    ax2.set_title("Heatmap + Contour Overlay")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_aspect("equal", adjustable="box")
    ax2.grid(True)

    # Clean colorbar on the side
    cax = fig.add_subplot(gs[2])
    fig.colorbar(img2, cax=cax, label='Point Density')

    plt.show()