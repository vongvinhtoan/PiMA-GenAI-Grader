import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pathlib import Path

dir_path = Path(__file__).resolve().parent

def plot_function_conture():
    # Create a grid of x, y values
    x = np.linspace(-4, 4, 400)
    y = np.linspace(-4, 4, 400)
    X, Y = np.meshgrid(x, y)
    
    Z = np.load(dir_path / 'Z.npy')

    # Plot the contour
    plt.figure(figsize=(8, 6))
    contours = plt.contourf(X, Y, Z, levels=10, cmap='inferno')

    cbar = plt.colorbar(contours)
    cbar.set_label('Function Value')
    plt.title("Heatmap of f(x, y)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axis("equal")
    plt.show()

def plot_function_derivative_vector_field():
    # Grid for vector field
    span = 35
    x = np.linspace(-4, 4, span)
    y = np.linspace(-4, 4, span)
    X, Y = np.meshgrid(x, y)

    # Load the function values from a file
    U = np.load(dir_path / 'U.npy')
    V = np.load(dir_path / 'V.npy')

    # Normalize the vector field
    magnitude = np.sqrt(U**2 + V**2)
    U_norm = np.divide(U, magnitude, out=np.zeros_like(U), where=magnitude != 0)
    V_norm = np.divide(V, magnitude, out=np.zeros_like(V), where=magnitude != 0)

    # Grid for contour (higher resolution)
    x_dense = np.linspace(-4, 4, 400)
    y_dense = np.linspace(-4, 4, 400)
    X_dense, Y_dense = np.meshgrid(x_dense, y_dense)

    Z = np.load(dir_path / 'Z.npy')

    # Create subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left plot: vector field
    q1 = ax1.quiver(X, Y, U_norm, V_norm, magnitude, cmap='Greys', scale=40)
    cb1 = fig.colorbar(q1, ax=ax1)
    cb1.set_label('Magnitude')
    ax1.set_title("Vector Field of ∇f(x, y)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.axis("equal")
    ax1.grid(True)

    # Right plot: vector field + contour
    contour = ax2.contour(X_dense, Y_dense, Z, levels=10, cmap='inferno', alpha=0.6)
    ax2.clabel(contour, inline=True, fontsize=8)
    q2 = ax2.quiver(X, Y, U_norm, V_norm, magnitude, cmap='Greys', scale=40)
    ax2.set_title("Vector Field with Contour Overlay")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.axis("equal")
    ax2.grid(True)

    plt.tight_layout()
    plt.show()
