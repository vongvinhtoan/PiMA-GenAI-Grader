import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def plot_function_conture():
    # Create a grid of x, y values
    x = np.linspace(-4, 4, 400)
    y = np.linspace(-4, 4, 400)
    X, Y = np.meshgrid(x, y)
    
    Z = np.load('Z.npy')

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
    U = np.load('U.npy')
    V = np.load('V.npy')

    # Normalize the vector field
    magnitude = np.sqrt(U**2 + V**2)
    U_norm = np.divide(U, magnitude, out=np.zeros_like(U), where=magnitude != 0)
    V_norm = np.divide(V, magnitude, out=np.zeros_like(V), where=magnitude != 0)

    # Grid for contour (higher resolution)
    x_dense = np.linspace(-4, 4, 400)
    y_dense = np.linspace(-4, 4, 400)
    X_dense, Y_dense = np.meshgrid(x_dense, y_dense)

    Z = np.load('Z.npy')

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

def plot_samples_with_contour(f, samples):
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

plot_function_conture()
plot_function_derivative_vector_field()